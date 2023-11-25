FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN apt-get update && apt-get install -y gcc libc-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local app directory to the working directory
COPY app/ .

# Command to run on container start
CMD ["python", "main.py"]
