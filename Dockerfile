# Start from the pre-built image on DockerHub
FROM hoopstreet/tiktok-prompt-generator:latest

USER root
WORKDIR /app

# Copy fresh application logic only
COPY . .

# Ensure HF permissions
RUN chown -R 1000:1000 /app
USER 1000

EXPOSE 7860
CMD ["python", "app.py"]
