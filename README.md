# Build command for the Langflow application
docker build -t langflow-app:latest .

# Run command to start the Langflow application
docker run -p 8080:8080 langflow-app:latest
