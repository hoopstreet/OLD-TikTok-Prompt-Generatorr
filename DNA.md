# 🧬 THE DNA BLUEPRINT: PHOENIX ARCHITECTURE
## Project: TikTok-Prompt-Generator
**Version:** v1.5.5-EXPANSION (Stable)
**Lead Developer:** hoopstreet

---

## 1. AI DEVELOPER CONSTRAINTS
(Guardrails as defined in v1.5.2)

---

## 2. THE "TRIPLE-SYNC" INFRASTRUCTURE
We utilize a Pinned-Version Architecture to ensure that code logic on GitHub, container images on Docker Hub, and the runtime on Hugging Face are always identical.

### 2.1 The Source of Truth (GitHub)
* **Private Logic:** Stores all Python backend, prompt templates, and scraping logic.
* **Orchestration:** GitHub Actions handle the heavy lifting of building and syncing.
* **Filtered Sync:** GitHub Actions automatically strip non-essential heavy files (e.g., /notebooks) before mirroring to Hugging Face to maintain the 10MB limit.

### 2.2 The Container Registry (Docker Hub)
* **Immutable Layers:** Every release is pinned to a specific version (e.g., v1.5.x-EXPANSION).
* **Zero Drift:** Direct version mapping between Git tags and Docker tags ensures the environment is locked.

### 2.3 The Deployment Target (Hugging Face Spaces)
* **Minimalist Footprint:** Contains ONLY Dockerfile and README.md.
* **Clean Room Execution:** HF acts as a headless runner, pulling the versioned image from Docker Hub.
* **Auto-Rebuild:** Triggered immediately when GitHub Actions push a version update to the HF repository.

---

## 12. DEPENDENCY LOCKING (STABILITY)
* **Transformers Policy:** Must be pinned to `v4.40.0` to maintain compatibility with Moondream2's custom Phi architecture.
* **Reasoning:** Newer versions (v4.50+) introduce breaking changes to `GenerationMixin` and `pad_token_id` requirements.

---

## 12. DEPENDENCY LOCKING (STABILITY)
* **Transformers Policy:** Must be pinned to `v4.40.0` to maintain compatibility with Moondream2's custom Phi architecture.
* **Reasoning:** Newer versions (v4.50+) introduce breaking changes to `GenerationMixin` and `pad_token_id` requirements.
