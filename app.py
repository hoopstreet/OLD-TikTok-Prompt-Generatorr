import gradio as gr
import os
import torch
from PIL import Image
import requests
from io import BytesIO
from supabase import create_client
from moondream.torch.hf_moondream import Moondream

# 1. Setup Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

# 2. Setup Moondream (Vision Engine)
model_id = "vikhyatk/moondream2"
model = Moondream.from_pretrained(model_id).to("cpu").eval()

def get_memory_and_training():
    train_data = supabase.table("training_materials").select("content").execute()
    train_context = "\n".join([item['content'] for item in train_data.data])
    
    history_data = supabase.table("chat_history").select("user_input,ai_response").order("created_at", desc=True).limit(3).execute()
    history_context = "\n".join([f"Input: {h['user_input']}\nAI: {h['ai_response']}" for h in history_data.data])
    
    return train_context, history_context

def process_tiktok_request(product_url, product_title, about_this_product, product_description, image_url):
    train_ctx, mem_ctx = get_memory_and_training()
    
    # Analyze Image via Moondream
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image_embeds = model.encode_image(image)
    image_description = model.answer_question(image_embeds, "Describe this product's appearance for a TikTok ad.", None)
    
    # Construct a high-detail prompt for the AI
    detailed_input = f"Title: {product_title}\nAbout: {about_this_product}\nDescription: {product_description}\nURL: {product_url}"
    
    prompt = (
        f"Style Guide: {train_ctx}\n"
        f"Memory: {mem_ctx}\n"
        f"Product Info: {detailed_input}\n"
        f"Visual Analysis: {image_description}\n\n"
        "Task: Generate a high-converting TikTok Affiliate script with a hook, body, and CTA."
    )
    
    # Generate Script
    final_script = model.answer_question(image_embeds, prompt, None)
    
    # Save to Supabase Chat History
    supabase.table("chat_history").insert({
        "user_input": product_title,
        "ai_response": final_script
    }).execute()
    
    return final_script

# Gradio Interface with your 5 specific fields
demo = gr.Interface(
    fn=process_tiktok_request,
    inputs=[
        gr.Textbox(label="Product URL"),
        gr.Textbox(label="Product Title"),
        gr.Textbox(label="About This Product"),
        gr.Textbox(label="Product Description"),
        gr.Textbox(label="Image URL")
    ],
    outputs=gr.Textbox(label="Viral TikTok Script"),
    title="TikTok Affiliate Professional Generator"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
