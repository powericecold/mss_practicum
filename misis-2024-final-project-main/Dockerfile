
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install gcc and python3-dev
RUN apt-get update && apt-get install -y gcc python3-dev

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run api.py when the container launches
CMD ["python", "api.py"]
