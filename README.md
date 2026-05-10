# ArchAgent: Local AI Assistant for Arch Linux & Hyprland

## 🔗 Links & Resources
* **Trained LoRA Adapters (Hugging Face):** [https://huggingface.co/13lanko/arch-assistant-final-lora/tree/main](https://huggingface.co/13lanko/arch-assistant-final-lora/tree/main)

![Arch Linux](https://img.shields.io/badge/OS-Arch_Linux-1793d1?style=flat-square&logo=arch-linux&logoColor=white)
![Hyprland](https://img.shields.io/badge/WM-Hyprland-00a896?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square&logo=python&logoColor=white)
![Unsloth](https://img.shields.io/badge/Framework-Unsloth-FF4B4B?style=flat-square)
![Model](https://img.shields.io/badge/Model-Qwen2.5--7B-yellow?style=flat-square)

**ArchAgent** is an experimental pipeline and local AI assistant designed specifically for Arch Linux, Hyprland, and Zsh power users. 

This project demonstrates how a smaller, open-source 7B parameter model can be trained to outperform generic base models in a highly specific niche. It utilizes a resource-efficient, multi-stage fine-tuning pipeline combining **Parameter-Efficient Fine-Tuning (PEFT)**, **Rejection Sampling Fine-Tuning (RSFT)**, and **Retrieval-Augmented Generation (RAG)**—all executable on consumer hardware (e.g., RTX 4080 Super).

---

## Project Goals & Philosophy

The primary goal of this project was to explore how to imbue a smaller model with both **domain-specific knowledge** and **advanced logical reasoning capabilities** without relying on massive compute clusters. 

While initially considering GRPO (Group Relative Policy Optimization) to teach reasoning patterns, the approach was pivoted to **Rejection Sampling Fine-Tuning (RSFT)** combined with **RLAIF (Reinforcement Learning from AI Feedback)**. This proved to be vastly more compute-efficient while achieving similar enhancements in the model's ability to "think" before it answers.

## Architecture & Training Pipeline

The project is built inside an isolated Docker container using `uv` for fast dependency management, and leverages the `unsloth` framework for 4-bit quantized training.

### Phase 1: Cold-Start SFT (Supervised Fine-Tuning)
* **Knowledge Distillation:** Generated ~1,100 high-quality synthetic samples (670 basic knowledge, 400 troubleshooting scenarios) using the DeepSeek-V4 API based on raw data from the Arch Wiki.
* **Formatting:** Enforced a strict XML-like schema (`<think>` for internal reasoning, `<answer>` for the final solution).
* **Training:** LoRA training on `qwen2.5-7b-instruct` achieved stable convergence, teaching the model the "Arch Linux tone" and complex dependencies (e.g., NVIDIA/Wayland quirks).

### Phase 2: RAG Pipeline Integration
* **Ingestion:** Parsed and chunked Markdown files from the official Arch and Hyprland Wikis using `RecursiveCharacterTextSplitter`.
* **Vector Store:** Implemented a local `ChromaDB` instance utilizing the `BAAI/bge-small-en-v1.5` embedding model.
* **Purpose:** To provide factual, up-to-date context to the LLM during both the RSFT training phase and final inference.

### Phase 3: RSFT (Rejection Sampling Fine-Tuning)
* **Generation:** Generated 6 distinct reasoning paths and answers for 1,000 prompts (500 RAG-augmented, 500 pure SFT) using the Phase 1 model.
* **RLAIF Filtering (LLM-as-a-Judge):** Sent all 6,000 outputs to the DeepSeek API to be strictly graded on format adherence and technical accuracy.
* **Refinement:** Filtered the dataset down to the top ~600 "Gold Standard" samples.
* **Final Training:** Executed a second SFT pass on this highly curated dataset to severely reduce hallucinations and perfect the RAG utilization.

---

## Evaluation & Benchmarks

To prove the efficacy of the pipeline, an ablation study was conducted. 50 completely unseen, highly specific Arch/Hyprland troubleshooting questions were generated. The Base model, the SFT model, and the RSFT model answered them using the exact same RAG context. The results were blindly evaluated by an API Judge (Scale 1-10).

| Model Stage | Format Adherence | Technical Accuracy | Helpfulness | **Overall Score** |
| :--- | :---: | :---: | :---: | :---: |
| **1. Base Model** | 9.7 | 4.3 | 5.0 | **6.3** |
| **2. SFT Model** | 8.2 | 5.3 | 5.8 | **6.4** |
| **3. RSFT Model** | **9.4** | **5.8** | **6.2** | **7.1** |

**Key Takeaways:**
* The **Base model** obeys format constraints well but heavily hallucinates technical solutions (Accuracy: 4.3).
* The **SFT model** learns technical concepts but suffers from an "alignment tax," struggling to balance new domain rules with strict formatting (Format dropped to 8.2).
* The **RSFT model** (with RAG context) is the clear winner. By filtering for high-quality reasoning paths, it recovers its format adherence (9.4) while reaching the highest technical accuracy and user helpfulness.

---

## Tech Stack
* **Base Model:** `Qwen/Qwen2.5-7B-Instruct`
* **Training:** PyTorch, Hugging Face Transformers, Unsloth (4-bit BNB)
* **RAG:** ChromaDB, HuggingFace Embeddings
* **Environment:** Docker, `uv`

---
