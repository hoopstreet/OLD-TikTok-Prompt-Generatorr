import re
import requests

class TikTokScraper:
    """Enhanced DNA Section 16 & 18: Multi-Format Extraction"""
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Referer": "https://www.tiktok.com/"
    }
    
    @staticmethod
    def extract_product_id(url):
        # Support for both /product/ID and /video/ID (where product is linked)
        prod_match = re.search(r'product/(\d+)', url)
        vid_match = re.search(r'video/(\d+)', url)
        return prod_match.group(1) if prod_match else (vid_match.group(1) if vid_match else None)

    @staticmethod
    def get_product_image_bytes(url):
        target_id = TikTokScraper.extract_product_id(url)
        if not target_id:
            return None
            
        # ByteDance CDN Object Store
        cdn_url = f"https://p16-item-sign.ibyteimg.com/obj/tiktok-obj/{target_id}~tplv-resize:480:480.webp"
        
        try:
            response = requests.get(cdn_url, headers=TikTokScraper.HEADERS, timeout=10)
            response.raise_for_status()
            return response.content
        except Exception as e:
            # Fallback for video-specific covers if product ID fails
            return None

if __name__ == "__main__":
    print("Multi-Format Scraper Active (Product/Video).")
