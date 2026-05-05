# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Define environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_DEFAULT_TIMEOUT=100

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the src directory contents into the container at /app
COPY src/ ./src/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application using uvicorn when the container launches
CMD ["uvicorn", "src.main:sinha_bank_api", "--host", "0.0.0.0", "--port", "8000"]