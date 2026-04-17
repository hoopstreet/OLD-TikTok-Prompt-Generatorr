import requests
import time

def process_batch(file_path):
    api_url = "https://huggingface.co/spaces/hoopstreet/TikTok-Prompt-Generator/process-tiktok"
    
    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
        
    print(f"🚀 Starting batch process for {len(urls)} items...")
    
    for url in urls:
        try:
            payload = {"url": url}
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                print(f"✅ Accepted: {url}")
            else:
                print(f"❌ Failed ({response.status_code}): {url}")
        except Exception as e:
            print(f"⚠️ Error connection to API: {e}")
        
        # Small delay to prevent rate-limiting on the n8n trigger
        time.sleep(1)

if __name__ == "__main__":
    # Create a dummy file for testing
    with open("links.txt", "w") as f:
        f.write("https://www.tiktok.com/view/product/7890123\n")
    
    process_batch("links.txt")
