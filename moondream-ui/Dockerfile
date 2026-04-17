FROM python:3.10-slim

# Setup user for Hugging Face
RUN useradd -m -u 1000 user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
WORKDIR $HOME/app

# Install git for any remote code dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy original requirements and install
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the original source code we pulled
COPY --chown=user . .

# Expose the standard HF port
EXPOSE 7860

# Run the original demo script (renamed to app.py)
CMD ["python", "app.py"]
