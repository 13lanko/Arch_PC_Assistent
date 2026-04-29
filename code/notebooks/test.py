from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Qwen/Qwen3-ASR-1.7B" # Ein kleines Modell zum Testen

print("Lade Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("Lade Modell auf die GPU...")
# Wir nutzen device_map="auto" damit Transformers die GPU erkennt
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    device_map="auto"
)

print(f"Modell ist geladen auf: {model.device}")

# Ein kleiner Test-Prompt
prompt = "hello!"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

output = model.generate(**inputs, max_new_tokens=50)
print("\nAntwort vom Modell:")
print(tokenizer.decode(output[0], skip_special_tokens=True))