FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOME=/home/user

# Create a non-root user for Hugging Face compatibility
RUN useradd -m -u 1000 user
WORKDIR $HOME/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt streamlit gradio transformers einops pillow

# Copy application files
COPY . .
RUN chown -R user:user $HOME/app

USER user

# Hugging Face Spaces default port
EXPOSE 7860

# Run the original Gradio UI
CMD ["python", "app.py"]
