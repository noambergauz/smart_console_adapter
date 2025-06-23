FROM python:3.12


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV API_BASE_URL=""
ENV DOMAIN=""

# Set the working directory
WORKDIR /app
# Install system dependencies
COPY smart_console_adapter/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY smart_console_adapter/smart_console_adapter /app/smart_console_adapter

CMD ["uvicorn", "smart_console_adapter.main:app", "--host", "0.0.0.0", "--port", "8000"]