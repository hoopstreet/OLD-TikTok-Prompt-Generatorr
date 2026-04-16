# Using standard Python base
FROM python:3.10-slim

# Install system dependencies for Moondream AND Image Compilation (Pillow-SIMD)
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    libsm6 \
    libxext6 \
    gcc \
    python3-dev \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Upgrade pip first to handle modern wheels
RUN pip install --upgrade pip

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Ensure HF permissions
RUN chown -R 1000:1000 /app
USER 1000

EXPOSE 7860
CMD ["python", "app.py"]
