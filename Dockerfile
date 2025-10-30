FROM python:3.11-slim

WORKDIR /app

# Set environment variables to prevent buffering
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
# Copy tools and config first for better caching
COPY ./config /app/config
COPY ./tools /app/tools
COPY ./agents /app/agents
COPY ./api /app/api

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
