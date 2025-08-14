FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app logic and server scripts
COPY app ./app
COPY trainer_api.py .
COPY predict_api.py .
COPY app/buy_computer_data.csv app/

# Default command (can override with CMD in docker-compose)
CMD ["uvicorn", "services.data_loader.load_data:app", "--host", "0.0.0.0", "--port", "8002"]