import gradio as gr
import os
import torch
from PIL import Image
import requests
from io import BytesIO
from supabase import create_client
from transformers import AutoConfig, AutoModelForCausalLM

# 1. Setup Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

# 2. Setup Moondream with v4.50+ Immunity
model_id = "vikhyatk/moondream2"

# FORCE THE CONFIG TO HAVE THE MISSING ATTRIBUTE
config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
config.pad_token_id = config.eos_token_id # Manually inject the missing ID

# Load using the patched config
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    config=config, 
    trust_remote_code=True,
    revision="main"
).to("cpu").eval()

def process_tiktok_request(product_url, product_title, about_this_product, product_description, image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image_embeds = model.encode_image(image)
    image_description = model.answer_question(image_embeds, "Describe this product for a TikTok ad.", None)
    
    prompt = f"Product: {product_title}\nVisuals: {image_description}\nTask: Viral TikTok Script."
    final_script = model.answer_question(image_embeds, prompt, None)
    
    supabase.table("chat_history").insert({"user_input": product_title, "ai_response": final_script}).execute()
    return final_script

demo = gr.Interface(
    fn=process_tiktok_request,
    inputs=[gr.Textbox(label="URL"), gr.Textbox(label="Title"), gr.Textbox(label="About"), gr.Textbox(label="Desc"), gr.Textbox(label="Img")],
    outputs=gr.Textbox(label="Script"),
    title="TikTok Affiliate Pro v1.8 - STABLE"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
