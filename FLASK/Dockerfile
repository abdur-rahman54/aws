# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY . .

# Install any necessary build dependencies temporarily
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000


# Command to run the Flask application when the container starts
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
