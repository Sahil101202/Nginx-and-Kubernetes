# Use the official Python image as a base
FROM sahil101202/ml-backend:latest

# Install pkg-config and HDF5
# Install build tools
RUN apt-get update && apt-get install -y \
    # Install pkg-config and HDF5
    pkg-config \
    libhdf5-dev \
    gcc \
    make \
    libc-dev

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
CMD ["python", "app.py"]
