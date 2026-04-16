# Use your pre-built image from DockerHub as the starting point
FROM hoopstreet/tiktok-prompt-generator:latest

# Switch to root to fix any permissions (Hugging Face needs this)
USER root

# Set the working directory inside the container
WORKDIR /app

# (Optional) Copy fresh code from GitHub if you made quick logic changes
# This allows you to update the app without rebuilding the whole DockerHub image
COPY . .

# Ensure the 'user' (UID 1000) owns the files (Hugging Face requirement)
RUN chown -R 1000:1000 /app

# Switch back to the non-root user
USER 1000

# Tell Hugging Face which port to look at
EXPOSE 7860

# Run your app
CMD ["python", "app.py"]
