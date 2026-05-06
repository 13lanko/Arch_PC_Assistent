# Project 1: arch_agent

## Overview:
An AI-powered, RAG-augmented system assistant for Arch Linux (Hyprland). Instead of acting as an unconstrained autonomous actor, the system focuses on structured reasoning, safe tool execution (Human-in-the-Loop), and acts as an experimental testbed to evaluate the effectiveness of Base Models vs. Fine-Tuned Models (SFT/GRPO) in a highly specific domain.

## Goal
The end-state objective is a robust, reasoning-capable assistant that leverages Retrieval-Augmented Generation (RAG) to maintain up-to-date knowledge of the Arch Linux ecosystem. A core scientific goal of this project is to empirically prove whether domain-specific SFT/GRPO provides a measurable advantage over base models when both have access to the same RAG context.

## Meta Intention
1. **Abstraction instead of specialization:** Create a framework for adaptive intelligence. Arch Linux serves as the “proof of concept”, but the architecture (Model + RAG + Tool-Calling) is generic enough to be adapted to any structured system by swapping the RAG database.
2. **Theorie-Transfer:** Practical application and validation of concepts from the Hugging Face ecosystem (SFT, LoRA, GRPO, RAG, LLM-as-a-Judge) in a real-world environment.
3. **Rigorous MLOps & Evaluation:** Moving away from "vibes-based" AI development towards structured, reproducible evaluations using automated metrics and hold-out test sets.
## Backlog:
1. This AI should work on both terminal and UI interface.
2. If this programme can work well, reduce the requirement of usage to run this with every local machine. (tiny version) 
3. This project should provide a pipeline for training assistent every setups (arch + any).


## To-Do:
### [x] Phase 1: SFT Cold Start & Foundation
* **Infrastructure & Environment**
    * [x] Docker container setup for isolated development
    * [x] Package management with `uv` for fast dependency resolution
    * [x] Integration of Unsloth for 4-bit quantized training on RTX 4080
* **Knowledge Distillation (Dataset)**
    * [x] Raw data extraction from Arch Wiki, (Hyprland Wiki), and GitHub
    * [x] Synthetic reasoning data generation via DeepSeek-v4 API
    * [x] Creation of a gold standard dataset (~1,100 samples)
        * [x] 670 Basic installation & configuration
        * [x] 400 Troubleshooting & recovery scenarios
* **Training & Validation**
    * [x] Execution of SFT training (3 epochs, LoRA r=16)
    * [x] Monitoring via TensorBoard (Loss convergence reached at ~0.7 - 0.8)
    * [x] Inference Check: Successful validation of the XML format (<think>/<answer>) and technical correctness (NVIDIA/Wayland fixes)

---

### [] Phase 2: GRPO Reasoning Optimization (Current Focus)
* **Reward Function Design**
    * [ ] Implementation of the Format Reward function (XML strictness)
    * [ ] Implementation of the Reasoning Length Reward (avoidance of "lazy reasoning")
    * [ ] Implementation of the Technical Accuracy Reward (validation of Arch keywords/syntax)
* **GRPO Training Setup**
    * [ ] Preparation of the prompt-only dataset (extraction of instructions without answers)
    * [ ] Configuration of the vLLM backend within Unsloth for group generation (G=8)
    * [ ] Execution of reinforcement training to reduce hallucinations
* **Evaluation**
    * [ ] Comparison test: SFT model vs. GRPO model (logic depth & error rate)

---

### [ ] Phase 3: Evaluation Framework & RAG Baseline (NEW PRIORITY)

* **Test Dataset Creation**
    * [ ] Create a hold-out test set of 50-100 real-world Arch/Hyprland scenarios (not included in Phase 1 training data).
* **LLM-as-a-Judge Implementation**
    * [ ] Set up an automated evaluation script using a strong judge model (e.g., Llama-3-70B, GPT-4o, or Claude).
    * [ ] Define scoring rubrics for Accuracy, Helpfulness, and Hallucination rate.
* **RAG Setup**
    * [ ] Implement a lightweight vector store (e.g., ChromaDB or FAISS) loaded with current Arch Wiki/Hyprland docs.
    * [ ] Test baseline performance: Evaluate Pretrained Qwen2.5-7B-Instruct (with and without RAG) against the Phase 1 SFT model (with and without RAG).