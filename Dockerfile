# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:v1.6.4-EXPANSION

# We use USER root
# Build Version: 1.6.4-EXPANSION
USER root
# Build Version: 1.6.4-EXPANSION
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
# Forced Refresh: Fri Apr 17 02:27:08 UTC 2026
