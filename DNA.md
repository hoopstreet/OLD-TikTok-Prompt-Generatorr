# 🧬 THE DNA BLUEPRINT: PHOENIX ARCHITECTURE
## Project: TikTok-Prompt-Generator
**Version:** v1.4.1-EXPANSION (Stable)
**Lead Developer:** hoopstreet
**Contact:** hoopstreet143@gmail.com

---

## 1. AI DEVELOPER CONSTRAINTS (THE GUARDRAILS)
To any AI assistant assisting in this project: **You are strictly prohibited from deviating from the established infrastructure.**
* **No "Latest" Tags:** Never suggest using :latest. All builds must be pinned to vX.X.X-EXPANSION.
* **Minimalist HF:** Do not suggest adding source code to Hugging Face. HF is a runner, not a storage unit.
* **Workflow Integrity:** Do not modify .github/workflows/ without explicitly confirming the "Two-Step Sync".
* **Atomic Logic:** Provide code updates that are modular. Do not merge infra logic with business logic.

---

## 2. THE "TRIPLE-SYNC" INFRASTRUCTURE
We utilize a Pinned-Version Architecture to ensure that GitHub, Docker Hub, and Hugging Face are always identical.

### 2.1 The Source of Truth (GitHub)
* **Private Logic:** All Python backend, prompt templates, and scraping logic.
* **Orchestration:** GitHub Actions handle the heavy lifting of building and syncing.

### 2.2 The Container Registry (Docker Hub)
* **Immutable Layers:** Every release is pinned to a specific version (e.g., v1.3.9-EXPANSION).
* **Zero Drift:** Direct version mapping between Git tags and Docker tags.

### 2.3 The Deployment Target (Hugging Face Spaces)
* **Minimalist Footprint:** Contains ONLY Dockerfile and README.md.
* **Clean Room Execution:** HF acts as a headless runner for the image on Docker Hub.

---

## 3. THE DEPLOYMENT LOOP (OPERATIONAL PROTOCOL)
Follow this exact sequence for every update to ensure zero downtime.

**3.1 Development (Local iSH)**
```bash
git add .
git commit -m "feat: [describe change]"
git push origin main
```

**3.2 Versioning (The Trigger)**
```bash
git tag -a v1.X.X-EXPANSION -m "Release: [Brief description]"
git push origin v1.X.X-EXPANSION
```

---

## 4. TECHNICAL INPUT PARSING (URL HANDLING)
The system is designed to accept and process high-complexity TikTok Shop data:
* **Image URL Handling:** Must accept ByteDance CDN links (*.ibyteimg.com) and recognize dynamic resizing parameters (e.g., resize-webp).
* **Product Link Handling:** Must accept TikTok Shop Product IDs (e.g., tiktok.com/view/product/...).
* **Data Extraction:** Prioritize the Product ID for unique storage in chat_history.

---

## 5. DATABASE MAINTENANCE (EDGE FUNCTIONS)
* **Auto-Cleanup:** A Supabase Edge Function deletes chat_history older than 30 days.
* **Storage Optimization:** Prevents database bloat via pg_cron every 24 hours.

---

## 6. ENVIRONMENT & SECURITY ARCHITECTURE
* **Zero-Hardcode Policy:** All connections must be mapped via Environment Variables (SUPABASE_URL, HF_TOKEN, etc.).
* **Runtime Logic:** AI must never output these secret values.

---

## 7. FAILURE RECOVERY (FIELD MANUAL)
**Error: [rejected] main -> main (fetch first)**
* **Fix:** `git pull origin main --rebase` then `git push origin main`.

---
**Last Updated:** April 17, 2026
**Authorized by:** Hoopstreet Sports Apparel Accessories Shop
