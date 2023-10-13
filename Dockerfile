# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the web server script into the container
COPY main.py ./main.py

# Install Flask
RUN pip install --no-cache-dir flask

# Command to run when the container starts
CMD ["python", "./main.py"]

