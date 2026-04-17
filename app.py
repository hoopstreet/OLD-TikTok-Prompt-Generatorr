import os
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from scraper import TikTokScraper
from database import SupabaseManager

app = FastAPI()
db = SupabaseManager()

class TikTokRequest(BaseModel):
    url: str

@app.get("/")
async def health():
    return {"status": "Phoenix Architecture Online", "version": "v1.5.9"}

@app.post("/process-tiktok")
async def process_tiktok(request: TikTokRequest, background_tasks: BackgroundTasks):
    product_id = TikTokScraper.extract_product_id(request.url)
    
    if not product_id:
        return {"error": "Invalid TikTok URL"}, 400

    # Log the incoming request to Supabase
    db.log_event("webhook_received", "processing", {"url": request.url, "id": product_id})

    # To keep n8n fast, we'll process the heavy AI stuff in the background
    background_tasks.add_task(run_inference_pipeline, product_id, request.url)

    return {"status": "accepted", "product_id": product_id}

def run_inference_pipeline(product_id, url):
    # This will be where we call Moondream in the next step
    db.log_event("inference_start", "pending", {"id": product_id})
    print(f"Pipeline started for {product_id}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
