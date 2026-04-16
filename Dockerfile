# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:v1.3.9-EXPANSION

# We use USER root
# Build Version: 1.3.9-EXPANSION
USER root
# Build Version: 1.3.9-EXPANSION
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
# Forced Refresh: Thu Apr 16 23:17:54 UTC 2026
