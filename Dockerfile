# This tells Hugging Face to pull your pre-built image from DockerHub
FROM ${DOCKERHUB_USERNAME}/tiktok-prompt-generator:latest

# We use USER root to ensure we can handle any file permissions inside the container
USER root
WORKDIR /app

# Ensure the app starts on the correct port for Hugging Face
EXPOSE 7860
CMD ["python", "app.py"]
