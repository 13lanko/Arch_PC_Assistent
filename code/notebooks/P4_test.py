import torch
import re
from unsloth import FastLanguageModel
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

import torch
from unsloth import FastLanguageModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pathlib import Path

persist_directory = "/workspaces/Arch_PC_Assistent/embed_model"
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
vectorstore = Chroma(embedding_function=embeddings,
                     persist_directory=persist_directory)

# ==========================================
# 1. SETUP: INITIALIZE RICH CONSOLE
# ==========================================
console = Console()

# ==========================================
# 2. SETUP: LOAD MODEL AND TOKENIZER
# ==========================================
model_path = "/workspaces/Arch_PC_Assistent/outputs/RSFT/arch_assistant_final_lora"
max_seq_length = 4096

with console.status("[bold green]Loading model into memory...", spinner="dots"):
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name = model_path,
        max_seq_length = max_seq_length,
        load_in_4bit = True,
    )
    FastLanguageModel.for_inference(model)

# ==========================================
# 3. SETUP: LOAD YOUR VECTOR STORE (RAG)
# ==========================================
# Insert your vectorstore initialization here.
# Example: vectorstore = Chroma(persist_directory="./db", embedding_function=embeddings)

console.print("[bold green]System is ready![/bold green]\n")

# ==========================================
# 4. THE MAIN CHAT LOGIC
# ==========================================
def ask_arch_agent(user_question):
    
    # --- Step A: Automatic Context Retrieval (RAG) ---
    docs = vectorstore.similarity_search(user_question, k=3)
    rag_context = "\n\n".join([f"--- Chunk {i+1} ({d.metadata.get('topic', 'unknown')}) ---\n{d.page_content}" for i, d in enumerate(docs)])
    
    # --- Step B: Build the Prompt ---
    system_prompt = f"""You are ArchAgent, an expert Arch Linux with hyprland and zsh setup assistant. 
Below is retrieved context from the Arch Wiki. Use this context as your primary source of truth to ensure accuracy.

CONTEXT:
{rag_context}

CRITICAL INSTRUCTIONS:
If the context is incomplete or does not fully cover the user's problem, you MUST seamlessly use your own internal knowledge to provide a complete solution.

Your output MUST strictly follow this exact format:
<think>
[Analyze the user's problem. Check what information is available in the context. If something is missing, retrieve it from your internal knowledge. Plan your solution.]
</think>
<answer>
[Your final, clear, and actionable answer here.]
</answer>"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_question}
    ]
    
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer([prompt], return_tensors="pt").to("cuda")

    # --- Step C: Generate Answer ---
    outputs = model.generate(
        **inputs,
        max_new_tokens=1024,
        use_cache=True,
        temperature=0.3,
        top_p=0.9
    )
    
    # --- Step D: Decode ---
    decoded_output = tokenizer.batch_decode(outputs[:, inputs["input_ids"].shape[1]:], skip_special_tokens=True)[0]
    
    return decoded_output

# ==========================================
# 5. PRETTY PRINTING AND INTERACTIVE TERMINAL
# ==========================================
from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import HTML

# ==========================================
# 5. PRETTY PRINTING AND INTERACTIVE TERMINAL
# ==========================================
# Create a session to handle history and advanced pasting
session = PromptSession()

while True:
    # Use prompt_toolkit instead of console.input()
    # HTML allows us to easily color the prompt text
    try:
        question = session.prompt(HTML("\n<b><ansicyan>[You]:</ansicyan></b> "))
    except (KeyboardInterrupt, EOFError):
        # Gracefully handle Ctrl+C or Ctrl+D
        console.print("[bold red]Exiting ArchAgent. Goodbye![/bold red]")
        break
    
    # Ignore empty inputs
    if not question.strip():
        continue
        
    if question.lower() in ["exit", "quit", "q"]:
        console.print("[bold red]Exiting ArchAgent. Goodbye![/bold red]")
        break
        
    with console.status("[bold yellow]ArchAgent is thinking and searching...", spinner="bouncingBar"):
        raw_output = ask_arch_agent(question)
    
    # --- The rest of your rich formatting code stays exactly the same ---
    think_match = re.search(r'<think>(.*?)</think>', raw_output, re.DOTALL)
    answer_match = re.search(r'<answer>(.*?)</answer>', raw_output, re.DOTALL)
    
    console.print("\n")
    
    if think_match:
        think_text = think_match.group(1).strip()
        console.print(Panel(Text(think_text, style="dim italic"), title="[dim]Internal Reasoning[/dim]", border_style="dim"))
    else:
        console.print("[dim italic]No <think> tags found.[/dim italic]")

    if answer_match:
        answer_text = answer_match.group(1).strip()
        markdown_answer = Markdown(answer_text)
        console.print(Panel(markdown_answer, title="[bold green]ArchAgent[/bold green]", border_style="green"))
    else:
        console.print(Panel(Markdown(raw_output), title="[bold red]Raw Output (Format Error)[/bold red]", border_style="red"))