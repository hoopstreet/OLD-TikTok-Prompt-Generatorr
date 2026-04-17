# 🧬 THE DNA BLUEPRINT: PHOENIX ARCHITECTURE
## Project: TikTok-Prompt-Generator
**Version:** v1.3.9-EXPANSION (Stable)
**Lead Developer:** hoopstreet
**Contact:** hoopstreet143@gmail.com

---

## 1. AI DEVELOPER CONSTRAINTS (THE GUARDRAILS)
To any AI assistant assisting in this project: **You are strictly prohibited from deviating from the established infrastructure.**
* **No "Latest" Tags:** Never suggest using `:latest`. All builds must be pinned to `vX.X.X-EXPANSION`.
* **Minimalist HF:** Do not suggest adding source code to Hugging Face. HF is a runner, not a storage unit.
* **Workflow Integrity:** Do not modify `.github/workflows/` without explicitly confirming the "Two-Step Sync" (Tag -> GitHub Edit -> HF Sync).
* **Atomic Logic:** Provide code updates that are modular. Do not merge infra logic with business logic.

---

## 2. THE "TRIPLE-SYNC" INFRASTRUCTURE
We utilize a **Pinned-Version Architecture** to ensure that code logic on GitHub, container images on Docker Hub, and the runtime on Hugging Face are always identical.

### 2.1 The Source of Truth (GitHub)
* **Private Logic:** All Python backend, prompt templates, and scraping logic.
* **Orchestration:** GitHub Actions handle the heavy lifting of building and syncing.

### 2.2 The Container Registry (Docker Hub)
* **Immutable Layers:** Every release is pinned to a specific version (e.g., `v1.3.9-EXPANSION`).
* **Zero Drift:** Direct version mapping between Git tags and Docker tags.

### 2.3 The Deployment Target (Hugging Face Spaces)
* **Minimalist Footprint:** Contains **ONLY** `Dockerfile` and `README.md`.
* **Clean Room Execution:** HF acts as a headless runner for the image on Docker Hub.

---

## 3. THE DEPLOYMENT LOOP (OPERATIONAL PROTOCOL)
Follow this exact sequence for every update to ensure zero downtime and zero configuration errors.

### 3.1 Development (Local iSH)
```bash
git add .
git commit -m "feat: [describe your change]"
git push origin main
```

### 3.2 Versioning (The Trigger)
```bash
git tag -a v1.X.X-EXPANSION -m "Release: [Brief description]"
git push origin v1.X.X-EXPANSION
```

### 3.3 Automated Chain Reaction
1. **`release-tag.yml`**: Builds Docker image -> Pushes Tag -> Edits GitHub Dockerfile text.
2. **`hf-sync.yml`**: Detects Dockerfile change -> Wipes HF files -> Force-pushes only Dockerfile & README.

---

## 4. CHANGE LOG & ROADMAP
* **v1.3.9 (CURRENT):** Removed `:latest` logic; enforced strict pinning; created DNA.md.
* **Phase 2:** Automated TikTok URL Scraping to Supabase (Pending).
* **Phase 3:** LTX-2 Turbo Video Generation Integration (Pending).

---

## 5. FAILURE RECOVERY (FIELD MANUAL)
**Error: `[rejected] main -> main (fetch first)`**
* **Cause:** The GitHub Action edited the Dockerfile on the server.
* **Fix:** `git pull origin main --rebase` then `git push origin main`.

---
**Last Updated:** April 17, 2026
**Authorized by:** Hoopstreet Sports Apparel Accessories Shop
