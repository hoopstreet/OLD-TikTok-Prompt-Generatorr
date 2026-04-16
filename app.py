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
    # Pull training materials
    train_data = supabase.table("training_materials").select("content").execute()
    train_context = "\n".join([item['content'] for item in train_data.data])
    
    # Pull last 3 chat interactions for memory
    history_data = supabase.table("chat_history").select("user_input,ai_response").order("created_at", desc=True).limit(3).execute()
    history_context = "\n".join([f"User: {h['user_input']}\nAI: {h['ai_response']}" for h in history_data.data])
    
    return train_context, history_context

def process_tiktok_request(product_details, image_url):
    train_ctx, mem_ctx = get_memory_and_training()
    
    # Analyze Image via Moondream
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image_embeds = model.encode_image(image)
    image_description = model.answer_question(image_embeds, "Describe this product and its key features for a TikTok ad.", None)
    
    # Create Final Prompt
    prompt = f"Training Info: {train_ctx}\nPast Memory: {mem_ctx}\nProduct: {product_details}\nVisuals: {image_description}\n\nTask: Create a viral TikTok script."
    
    # Simulate Script Generation (You can plug in an LLM here or use Moondream for text)
    final_script = f"Generated Script for {product_details}: " + model.answer_question(image_embeds, prompt, None)
    
    # Save to Supabase Chat History
    supabase.table("chat_history").insert({
        "user_input": product_details,
        "ai_response": final_script
    }).execute()
    
    return final_script

# Gradio Interface
demo = gr.Interface(
    fn=process_tiktok_request,
    inputs=[gr.Textbox(label="Product Details"), gr.Textbox(label="Image URL")],
    outputs=gr.Textbox(label="Viral TikTok Script"),
    title="TikTok Prompt Generator (Vision + Memory)"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
