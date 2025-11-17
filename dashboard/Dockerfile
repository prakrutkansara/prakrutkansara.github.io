FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for cartopy
RUN apt-get update && apt-get install -y \
    libgeos-dev \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and data
COPY app_hf.py app.py
COPY data/ data/

# Hugging Face Spaces uses port 7860
EXPOSE 7860

# Set environment variable for Hugging Face
ENV PORT=7860

CMD ["python", "app.py"]
