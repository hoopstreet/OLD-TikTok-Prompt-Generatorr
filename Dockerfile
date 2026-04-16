# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:v1.3.5-EXPANSION

# We use USER root
# Build Version: 1.7.2 to ensure we can handle any file permissions inside the container
USER root
# Build Version: 1.7.2
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
# Forced Refresh: Thu Apr 16 22:01:14 UTC 2026
