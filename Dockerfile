# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY scripts/ ./scripts/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the script
CMD ["python", "scripts/update_weather.py"] 