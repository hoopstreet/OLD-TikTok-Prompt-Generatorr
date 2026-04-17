import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from scraper import TikTokScraper
from database import SupabaseManager
from inference import MoondreamInference

app = FastAPI()
db = SupabaseManager()
engine = MoondreamInference()

class TikTokRequest(BaseModel):
    url: str

@app.get("/")
async def health():
    return {"status": "Phoenix Architecture Online", "version": "v1.6.1"}

@app.post("/process-tiktok")
async def process_tiktok(request: TikTokRequest, background_tasks: BackgroundTasks):
    product_id = TikTokScraper.extract_product_id(request.url)
    if not product_id:
        return {"error": "Invalid TikTok URL"}, 400

    db.log_event("webhook_received", "processing", {"url": request.url, "id": product_id})
    background_tasks.add_task(run_inference_pipeline, product_id, request.url)
    return {"status": "accepted", "product_id": product_id}

def run_inference_pipeline(product_id, url):
    try:
        # 1. Scrape (Simulated for now, would use TikTokScraper logic)
        image_url = url # This would normally be the CDN image URL
        
        # 2. AI Inference
        prompt = engine.generate_prompt(image_url)
        
        # 3. Save to Supabase
        db.save_product(
            product_id=product_id,
            product_name="TikTok Product", # Dynamic name logic next
            raw_json={"source_url": url},
            prompt=prompt
        )
        db.log_event("inference_complete", "success", {"id": product_id})
    except Exception as e:
        db.log_event("inference_failed", "error", {"id": product_id, "error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
