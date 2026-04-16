import gradio as gr
import os
from supabase import create_client

# Cloud Connections
supabase = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))

def generate_video_prompt(product_details, image_url):
    # This runs on Hugging Face using your DockerHub environment
    # Logic for TikTok hooks goes here
    result = f"Viral Hook for: {product_details}"
    return result

demo = gr.Interface(fn=generate_video_prompt, inputs=["text", "text"], outputs="text")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
