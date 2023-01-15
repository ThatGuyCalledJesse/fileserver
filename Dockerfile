# Use an official Alpine Linux as a parent image
FROM alpine:latest

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . .

# Run the start_server.sh script
CMD ["sh", "start_server.sh"]
