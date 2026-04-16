import gradio as gr
import os
import torch
from PIL import Image
import requests
from io import BytesIO
from supabase import create_client
# This is your original local import
from moondream.torch.hf_moondream import Moondream
from transformers import AutoConfig

# 1. Setup Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

# 2. Setup Moondream (Vision Engine)
model_id = "vikhyatk/moondream2"

# --- THE ONLY FIX NEEDED FOR v4.50 ---
config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
if not hasattr(config, "pad_token_id"):
    config.pad_token_id = 50256
# -------------------------------------

model = Moondream.from_pretrained(model_id).to("cpu").eval()

def get_memory_and_training():
    try:
        train_data = supabase.table("training_materials").select("content").execute()
        train_context = "\n".join([item['content'] for item in train_data.data])
        history_data = supabase.table("chat_history").select("user_input,ai_response").order("created_at", desc=True).limit(3).execute()
        history_context = "\n".join([f"Input: {h['user_input']}\nAI: {h['ai_response']}" for h in history_data.data])
        return train_context, history_context
    except:
        return "", ""

def process_tiktok_request(product_url, product_title, about_this_product, product_description, image_url):
    train_ctx, mem_ctx = get_memory_and_training()
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image_embeds = model.encode_image(image)
    image_description = model.answer_question(image_embeds, "Describe this product's appearance for a TikTok ad.", None)
    
    prompt = f"Style Guide: {train_ctx}\nMemory: {mem_ctx}\nProduct: {product_title}\nVisuals: {image_description}\nTask: Viral TikTok Script."
    final_script = model.answer_question(image_embeds, prompt, None)
    
    supabase.table("chat_history").insert({"user_input": product_title, "ai_response": final_script}).execute()
    return final_script

demo = gr.Interface(
    fn=process_tiktok_request,
    inputs=[gr.Textbox(label="URL"), gr.Textbox(label="Title"), gr.Textbox(label="About"), gr.Textbox(label="Desc"), gr.Textbox(label="Img")],
    outputs=gr.Textbox(label="Script"),
    title="TikTok Affiliate Pro v1.7.2"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
