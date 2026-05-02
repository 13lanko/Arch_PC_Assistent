# Project 1: arch_agent

## Overview:
An autonomous, AI-powered system manager for Arch Linux (Hyprland) that handles complex configuration and troubleshooting tasks through logical reasoning and active system access.

## Goal
The end-state objective is a Reasoning-Capable Autonomous System Agent specifically optimized for the Arch Linux ecosystem. The model will function as a high-level controller capable of mapping abstract user intent to precise system-state transition.

## Meta Intention
1. **Abstraction instead of specialization:** Create a framework for adaptive intelligence. Arch Linux serves as your “proof of concept” (the first application), but the architecture is so generic that it can be adapted to any structured system (OS, software suites, cloud infrastructure) by swapping out the knowledge module (retraining or RAG).
2. **Theorie-Transfer:** Practical application and validation of concepts from the Hugging Face ecosystem (fine-tuning, LoRA, agentic workflows) in a real-world system environment.

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

### [] Phase 3: Agentic Integration & System Access
* **Tool Environment**
    * [ ] Development of a "Safe Execution Environment" for shell commands
    * [ ] Connection to Hyprland IPC for real-time UI control
* **Interface**
    * [ ] Development of the CLI controller (`arch-agent` command)
    * [ ] Optional GUI integration for visual troubleshooting
* **Optimization**
    * [ ] "Tiny Version" porting (model distillation to 1.5B or 3B for local low-end machines)