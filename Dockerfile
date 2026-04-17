# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:v1.8.0-MOONDREAM

# We use USER root
# Build Version: 1.8.0-MOONDREAM
USER root
# Build Version: 1.8.0-MOONDREAM
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
# Forced Refresh: Fri Apr 17 14:09:34 UTC 2026
