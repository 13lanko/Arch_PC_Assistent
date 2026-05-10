# Project 1: arch_agent

## Overview:
An AI-powered, RAG-augmented system assistant for Arch Linux (Hyprland). Instead of acting as an unconstrained autonomous actor, the system focuses on structured reasoning and acts as an experimental testbed to evaluate the effectiveness of Base Models vs. Fine-Tuned Models (SFT/RSFT) in a highly specific domain.

## Goal
The end-state objective is a robust, reasoning-capable assistant that leverages Retrieval-Augmented Generation (RAG) to maintain up-to-date knowledge of the Arch Linux ecosystem. A core scientific goal of this project is to empirically prove whether domain-specific SFT/RSFT provides a measurable advantage over base models when both have access to the same RAG context.

## Meta Intention
1. **Theorie-Transfer:** Practical application and validation of concepts from the Hugging Face ecosystem (SFT, LoRA, RSFT, RAG, LLM-as-a-Judge, GRPO, RSFT) in a real-world environment.
2. **Rigorous MLOps & Evaluation:** Moving away from "vibes-based" AI development towards structured, reproducible evaluations using automated metrics and hold-out test sets.


## To-Do:
### [x] Phase 1: SFT Cold Start & Foundation
* **Infrastructure & Environment**
    * [x] Docker container setup for isolated development
    * [x] Package management with `uv` for fast dependency resolution
    * [x] Integration of Unsloth for 4-bit quantized training on RTX 4080
* **Knowledge Distillation (Dataset)**
    * [x] Raw data extraction from Arch Wiki, (Hyprland Wiki), and GitHub
    * [x] Concatenate all extracted raw data into one file, clearly separating each topic
    * [x] Synthetic reasoning data generation via DeepSeek-v4 API with rigorous prompt structure based on the extraced raw datas
    * [x] Creation of a gold standard dataset (~1,100 samples)
        * [x] 670 Basic installation & configuration
        * [x] 400 Troubleshooting & recovery scenarios
* **Training**
    * [x] Execution of SFT training (3 epochs, LoRA r=16)
    * [x] Monitoring via TensorBoard (Loss convergence reached at ~0.7 - 0.8)

---

### [x] Phase 2: RAG Pipeline Setup (Retrieval-Augmented Generation)
* **Data Ingestion**
    * [x] Download raw documentation in Markdown format (has been already done in phase 1).
* **Intelligent Chunking**
    * [x] Implement a text splitter using `RecursiveCharacterTextSplitter` to keeps content intact and prevent hard cuts within same topic.
    * [x] Define chunk size (1000 tokens) and overlap size (200 tokens) to balance context quality and VRAM limits (which is not be tested for the optimal performance).
* **Vector Store & Embedding**
    * [x] Set up a local embedding model optimized for code/technical text (BAAI/bge-small-en-v1.5).
    * [x] Initialize a local vector database (ChromaDB) and ingest the chunked Markdown files.
* **Retrieval Scripting**
    * [x] Write a Python function that takes a user query, retrieves the Top-K (Top 4) chunks from ChromaDB, and injects them into the System Prompt.

---

### [x] Phase 3: RSFT Optimization (Rejection Sampling Fine-Tuning)
* **Prompts generation**
    * [x] write a rigorous prompt structure to generate ~1,000 prompts for the RSFT Optimization
        * [x] 500 prompts extracted from the previous gold standard dataset for the SFT
        * [x] 500 new Synthetic prompt via Deepseek API
* **Context-Aware Offline Generation**
    * [x] Run the ~1,000 prompts through the RAG pipeline (Phase 2) to append factual context to each prompt.
    * [x] Generate $G=6$ different reasoning paths and answers per prompt locally via the finetuned model (using higher temperature for variance).
* **LLM-as-a-Judge Evaluation (RLAIF)**
    * [x] Define a strict scoring rubric (JSON schema) focusing on Accuracy and Format.
    * [x] Send the generated answers to the DeepSeek-V4-Pro API for automated, high-quality scoring.
* **Data Filtering & Formatting**
    * [x] Write a script to filter the DeepSeek results: Discard any answer that does not achieve a near-perfect score (The "Rejection" step).
    * [x] Format the remaining "Gold Standard" answers into a new SFT-ready JSONL dataset (~600 samples).
* **RSFT Training Execution**
    * [x] Run a second SFT pass exclusively on this filtered, high-quality dataset to refine the model's logical reasoning and RAG capabilities.

---

### [x] Phase 4: Ablation Study & Final Evaluation (LLM-as-a-Judge)
* **Test Dataset Generation**
    * [x] Creation of a Python script to generate 50 new benchmark questions via DeepSeek API.
* **Multi-Model Inference Pipeline**
    * [x] Development of an automated inference script that iterates through the 50 questions.
    * [x] RAG Integration: Automatic context retrieval for each question.
    * [x] Run 1: Generate answers with the untuned base model (Zero-point measurement).
    * [x] Run 2: Generate answers with the pure SFT model (1,100 samples).
    * [x] Run 3: Generate answers with the final RSFT model (600 samples).
    * [x] Save all results (Question, RAG Context, Base Answer, SFT Answer, RSFT Answer) in a structured JSON file.
* **The Automated Tribunal (DeepSeek API)**
    * [x] Definition of a strict JSON scoring rubric (scores from 0-10 for format adherence, technical accuracy, and helpfulness).
    * [x] Programming of the judge script: DeepSeek evaluates the 3 answers per question blindly against each other.
* **Analysis & Conclusion**
    * [x] Evaluation of metrics (average scores per model).
    * [x] Documentation of performance gains (Base → SFT → RSFT) to verify the effectiveness of each fine-tuning stage.