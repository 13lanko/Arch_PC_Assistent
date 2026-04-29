# NVIDIA CUDA Basis-Image für Deep Learning
FROM nvidia/cuda:12.1.1-devel-ubuntu22.04

# uv installieren (schneller als pip)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# System-Abhängigkeiten installieren
RUN apt-get update && apt-get install -y python3-dev python3-pip git

WORKDIR /app

# PyTorch und wichtigste LLM-Tools vorab installieren (spart Zeit beim Sync)
RUN uv pip install --system torch transformers accelerate datasets
