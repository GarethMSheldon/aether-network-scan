# Use a highly optimized Python Alpine image
FROM python:3.11-alpine

# Set tool directory
WORKDIR /app

# Create logs directory for persistent storage
RUN mkdir -p /app/logs

# Copy source code
COPY src/ .

# Ensure logs directory is writable
RUN chmod 777 /app/logs

# Set Environment defaults
ENV SCAN_TARGET=127.0.0.1
ENV SCAN_PORTS=1-1024
ENV SCAN_TIMEOUT=0.5
ENV MAX_THREADS=50

# Execute AETHER-SCAN
ENTRYPOINT ["python", "main.py"]
