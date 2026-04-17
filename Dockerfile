# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:v1.7.5-EXPANSION

# We use USER root
# Build Version: 1.7.5-EXPANSION
USER root
# Build Version: 1.7.5-EXPANSION
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
# Forced Refresh: Fri Apr 17 02:44:10 UTC 2026
