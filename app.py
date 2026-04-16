import gradio as gr
import os
from supabase import create_client

# Cloud Connections
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

def get_training_context():
    # Pulls your training materials from Supabase
    data = supabase.table("training_materials").select("content").execute()
    return "\n".join([item['content'] for item in data.data])

def generate_tiktok_prompt(product_details, image_url):
    # Get training materials for context
    context = get_training_context()
    
    # Moondream logic would go here to analyze image_url
    # For now, we combine the details with your training rules
    final_prompt = f"Using these materials: {context}\n\nCreate a TikTok script for: {product_details}"
    
    return final_prompt

demo = gr.Interface(
    fn=generate_tiktok_prompt, 
    inputs=["text", "text"], 
    outputs="text",
    title="TikTok Affiliate AI Generator"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
