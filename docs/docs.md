# Project 1: arch_agent

## Overview:
An AI-powered, RAG-augmented system assistant for Arch Linux (Hyprland). Instead of acting as an unconstrained autonomous actor, the system focuses on structured reasoning, safe tool execution (Human-in-the-Loop), and acts as an experimental testbed to evaluate the effectiveness of Base Models vs. Fine-Tuned Models (SFT/RSFT) in a highly specific domain.

## Goal
The end-state objective is a robust, reasoning-capable assistant that leverages Retrieval-Augmented Generation (RAG) to maintain up-to-date knowledge of the Arch Linux ecosystem. A core scientific goal of this project is to empirically prove whether domain-specific SFT/RSFT provides a measurable advantage over base models when both have access to the same RAG context.

## Meta Intention
1. **Abstraction instead of specialization:** Create a framework for adaptive intelligence. Arch Linux serves as the “proof of concept”, but the architecture (Model + RAG + Tool-Calling) is generic enough to be adapted to any structured system by swapping the RAG database.
2. **Theorie-Transfer:** Practical application and validation of concepts from the Hugging Face ecosystem (SFT, LoRA, RSFT, RAG, LLM-as-a-Judge) in a real-world environment.
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

### [ ] Phase 2: RAG Pipeline Setup (Retrieval-Augmented Generation)
* **Data Ingestion**
    * [x] Download raw documentation in Markdown format (has been already done in phase 1).
* **Intelligent Chunking**
    * [ ] Implement a text splitter (e.g., via LangChain) that respects Markdown headers (##) and keeps bash/config code blocks intact.
    * [ ] Define optimal chunk size (e.g., ~500 tokens) to balance context quality and VRAM limits.
* **Vector Store & Embedding**
    * [ ] Set up a local embedding model optimized for code/technical text (e.g., nomic-embed-text or bge-m3).
    * [ ] Initialize a local vector database (e.g., ChromaDB) and ingest the chunked Markdown files.
* **Retrieval Scripting**
    * [ ] Write a Python function that takes a user query, retrieves the Top-K (e.g., Top 3) chunks from ChromaDB, and injects them into the System Prompt.

---

### [ ] Phase 3: RSFT Optimization (Rejection Sampling Fine-Tuning)
* **Context-Aware Offline Generation**
    * [ ] Run the ~1,000 prompts through the RAG pipeline (Phase 2) to append factual context to each prompt.
    * [ ] Generate $G=6$ different reasoning paths and answers per prompt locally via the finetuned model (using higher temperature for variance).
* **LLM-as-a-Judge Evaluation (RLAIF)**
    * [ ] Define a strict scoring rubric (JSON schema) focusing on Accuracy, Format, and Helpfulness.
    * [ ] Send the generated answers to the DeepSeek-V4-Pro API for automated, high-quality scoring.
* **Data Filtering & Formatting**
    * [ ] Write a script to filter the DeepSeek results: Discard any answer that does not achieve a near-perfect score (The "Rejection" step).
    * [ ] Format the remaining "Gold Standard" answers into a new SFT-ready JSONL dataset.
* **RSFT Training Execution**
    * [ ] Run a second SFT pass (using Unsloth) exclusively on this filtered, high-quality dataset to refine the model's logical reasoning and tool-use capabilities.