# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:v1.3.7-EXPANSION

# We use USER root
# Build Version: 1.3.7-EXPANSION
USER root
# Build Version: 1.3.7-EXPANSION
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
# Forced Refresh: Thu Apr 16 22:57:37 UTC 2026
