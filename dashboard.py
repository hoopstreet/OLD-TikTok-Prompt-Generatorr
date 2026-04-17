import streamlit as st
from database import SupabaseManager
import pandas as pd

# Page Config for Mobile responsiveness
st.set_page_config(page_title="Hoopstreet AI Dashboard", layout="wide")

st.title("🚀 TikTok Product Gallery")
st.markdown("### Browse Moondream-Generated Viral Prompts")

db = SupabaseManager()

def load_data():
    # Fetching latest 50 items from your products table
    response = db.client.table("products").select("*").order("created_at", desc=True).limit(50).execute()
    return response.data

data = load_data()

if not data:
    st.warning("No products found in Supabase. Run the scraper first!")
else:
    # Create a grid layout
    cols = st.columns(2) if st.sidebar.checkbox("Mobile View", True) else st.columns(3)
    
    for idx, item in enumerate(data):
        with cols[idx % len(cols)]:
            st.image(item.get("image_url", "https://via.placeholder.com/480"), use_column_width=True)
            st.info(f"**ID:** {item['product_id']}")
            with st.expander("View Viral Prompt"):
                st.write(item.get("prompt", "No prompt generated yet."))
            st.divider()

if st.button("🔄 Refresh Data"):
    st.rerun()
