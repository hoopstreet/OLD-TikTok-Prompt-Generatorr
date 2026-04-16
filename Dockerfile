# This tells Hugging Face to pull your pre-built image from DockerHub
FROM hoopstreet/tiktok-prompt-generator:latest

# We use USER root
# Build Version: 1.7.1 to ensure we can handle any file permissions inside the container
USER root
# Build Version: 1.7.1
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
