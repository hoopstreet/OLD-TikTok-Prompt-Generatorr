# Using standard Python base for the FIRST successful build
FROM python:3.10-slim

# Install system dependencies needed for Moondream/Vision
RUN apt-get update && apt-get install -y     git     ffmpeg     libsm6     libxext6     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install requirements (This takes a while the first time)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Ensure HF permissions
RUN chown -R 1000:1000 /app
USER 1000

EXPOSE 7860
CMD ["python", "app.py"]
