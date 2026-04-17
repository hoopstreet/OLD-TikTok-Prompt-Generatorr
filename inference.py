import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
from io import BytesIO

class MoondreamInference:
    def __init__(self):
        self.model_id = "vikhyatk/moondream2"
        self.revision = "2024-03-06"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load model with local code trust for custom Phi architecture
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id, revision=self.revision)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id, 
            trust_remote_code=True, 
            revision=self.revision
        ).to(self.device)
        self.model.eval()

    def generate_prompt(self, image_url, query="Act as a viral TikTok Shop Influencer. Analyze this product image and list 3 high-energy selling points, its aesthetic appeal, and a target niche. Use catchy language. Also, provide a 1-sentence scroll-stopping caption and 5 trending hashtags."):
        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            
            # Encapsulate the vision-to-text logic
            with torch.no_grad():
                image_embeds = self.model.encode_image(image)
                answer = self.model.answer_question(image_embeds, query, self.tokenizer)
            return answer
        except Exception as e:
            return f"Inference Error: {str(e)}"

if __name__ == "__main__":
    print("Inference Engine Initialized. Device:", torch.cuda.is_available())
