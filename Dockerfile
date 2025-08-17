# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service code
COPY services ./services

# Expose the port FastAPI will run on
EXPOSE 8002

# Run FastAPI
CMD ["uvicorn", "services.data_loader.load_data:app", "--host", "0.0.0.0", "--port", "8002"]
