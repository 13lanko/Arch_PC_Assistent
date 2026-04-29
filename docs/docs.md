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

## Phases:
1. Train a reasoning model on your own by applying GRPO []
2. Build a RAG to extent the model knowledge []
3. Build a Agent using the trained model to achieve system access []

## To-Do:
- # Phase 1:
  - Set the project environment using Docker [x]
  - Base model loading [x]
  - Set a set of evaluation tasks []
  - Test the performance of the pretrained model using the eval-tasks []
  - provide a set of dataset for the Cold-Start SFT []
  - provide a set of prompt library for the RL []
  - set the reward rule for the GRPO []
  - train the model []
  - evaluate the trained model using eval-tasks []
  - compare the performance between the pretrained and the fine-tuned model []
