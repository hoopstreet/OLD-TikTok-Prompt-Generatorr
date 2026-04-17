# 🧬 THE DNA BLUEPRINT: PHOENIX ARCHITECTURE
## Project: TikTok-Prompt-Generator
**Version:** v1.5.0-EXPANSION (Stable)
**Lead Developer:** hoopstreet
**Contact:** hoopstreet143@gmail.com

---

## 1. AI DEVELOPER CONSTRAINTS (THE GUARDRAILS)
To any AI assistant assisting in this project: **You are strictly prohibited from deviating from the established infrastructure.**
* **No "Latest" Tags:** Never suggest using `:latest`. All builds must be pinned to `vX.X.X-EXPANSION` to prevent environment drift.
* **Minimalist HF:** Do not suggest adding source code to Hugging Face. HF is a runner, not a storage unit.
* **Workflow Integrity:** Do not modify `.github/workflows/` without explicitly confirming the "Two-Step Sync" (Tag -> GitHub Edit -> HF Sync).
* **Atomic Logic:** Provide code updates that are modular. Do not merge infra logic with business logic.

---

## 2. THE "TRIPLE-SYNC" INFRASTRUCTURE
We utilize a Pinned-Version Architecture to ensure that code logic on GitHub, container images on Docker Hub, and the runtime on Hugging Face are always identical.

### 2.1 The Source of Truth (GitHub)
* **Private Logic:** Stores all Python backend, prompt templates, and scraping logic.
* **Orchestration:** GitHub Actions handle the heavy lifting of building and syncing.
* **Connection:** Pushes to Docker Hub via secret credentials.

### 2.2 The Container Registry (Docker Hub)
* **Immutable Layers:** Every release is pinned to a specific version (e.g., `v1.5.0-EXPANSION`).
* **Zero Drift:** Direct version mapping between Git tags and Docker tags.

### 2.3 The Deployment Target (Hugging Face Spaces)
* **Minimalist Footprint:** Contains ONLY `Dockerfile` and `README.md`.
* **Clean Room Execution:** HF acts as a headless runner, pulling the versioned image from Docker Hub.

---

## 3. TOOLSET & CONNECTION MAPPING
The system relies on a mesh of decentralized tools to maintain a 24/7 uptime without a physical server.

| Tool | Role | Primary Connection |
| :--- | :--- | :--- |
| **iSH (iPhone)** | Local Terminal | SSH/Git access to GitHub (Control Center) |
| **GitHub** | CI/CD Hub | Triggers Docker Hub builds & HF Space updates |
| **Docker Hub** | Image Storage | Receives builds from GitHub; Feeds HF |
| **Hugging Face** | Compute Runner | Pulls images from Docker Hub for execution |
| **Supabase** | DB & Backend | Stores `chat_history`, niche memory, & logs |
| **n8n** | Automation | Orchestrates URL scraping & DB synchronization |

---

## 4. TECHNICAL INPUT PARSING (URL HANDLING)
The system is designed to accept and process high-complexity TikTok Shop data:
* **Image URL Handling:** Must accept ByteDance CDN links (`*.ibyteimg.com`). The AI must recognize that these links contain dynamic resizing parameters (e.g., `resize-webp`) and security tokens.
* **Product Link Handling:** Must accept TikTok Shop Product IDs (e.g., `tiktok.com/view/product/...`).
* **Data Extraction:** The AI should prioritize the Product ID from the link to ensure it stores a unique identifier in the `chat_history` database for memory retrieval.

---

## 5. DATABASE MAINTENANCE (EDGE FUNCTIONS)
* **Auto-Cleanup:** A Supabase Edge Function is active to delete `chat_history` older than 30 days.
* **Storage Optimization:** Prevents database bloat while maintaining enough context for Niche Isolation.
* **Execution:** Runs via `pg_cron` every 24 hours.

---

## 6. ENVIRONMENT & SECURITY ARCHITECTURE
The system relies on a **Zero-Hardcode policy**.
* **Database (Supabase):** Pulls from `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`.
* **Deployment (CI/CD):** Uses `HF_TOKEN` and `DOCKERHUB_USERNAME` for automated pushes.
* **Runtime Logic:** The AI must never output these values. It only uses them to authenticate its connection.

---

## 7. FAILURE RECOVERY (FIELD MANUAL)
**Error: [rejected] main -> main (fetch first)**
* **Cause:** Remote repository has changes (usually from GitHub Actions) not present locally.
* **Fix:** `git pull origin main --rebase` then `git push origin main`.

---

## 8. MOBILE DEVELOPMENT PROTOCOL (iSH/iPhone)
* **Zero Manual Edits:** AI must provide full code via `cat <<EOF` for direct terminal injection. No manual keyboard editing required.
* **Remote-First:** Code must focus on remoting to GitHub. Do not run heavy local processes (npm, etc.) to prevent iPhone memory hanging.
* **Character Limits:** If code exceeds mobile paste limits, AI must split into Parts.
* **Automation:** All logic must be inserted/edited directly into target files via automated scripts.
* **Project Focus:** All development must strictly target the **TikTok-Prompt-Generator**.

---
**Last Updated:** April 17, 2026
**Authorized by:** Hoopstreet Sports Apparel Accessories Shop
