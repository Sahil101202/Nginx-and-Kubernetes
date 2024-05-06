# Use the official Python image as a base
FROM python:3.8-slim

# Install pkg-config and HDF5
RUN apt-get update && \
    apt-get install -y pkg-config && \
    apt-get install -y libhdf5-dev

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

RUN pip install --upgrade pip
# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port the application runs on
EXPOSE 5000

# Command to run the Python script
CMD ["python", "ml_model.py"]
