import re
import requests

class TikTokScraper:
    """Enhanced DNA Section 4 & 16: Mobile-Spoofed Extraction"""
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.tiktok.com/"
    }
    
    @staticmethod
    def extract_product_id(url):
        match = re.search(r'product/(\d+)', url)
        return match.group(1) if match else None

    @staticmethod
    def get_product_image_bytes(url):
        product_id = TikTokScraper.extract_product_id(url)
        if not product_id:
            return None
            
        cdn_url = f"https://p16-item-sign.ibyteimg.com/obj/tiktok-obj/{product_id}~tplv-resize:480:480.webp"
        
        try:
            # Use headers to bypass 403 Forbidden
            response = requests.get(cdn_url, headers=TikTokScraper.HEADERS, timeout=10)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"Scraper Error: {e}")
            return None

if __name__ == "__main__":
    print("Scraper Spoofing Active. User-Agent: iPhone/Safari")
