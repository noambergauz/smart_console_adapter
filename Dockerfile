FROM python:3.12


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV API_BASE_URL=""
ENV DOMAIN=""

# Set the working directory
WORKDIR /tmp/app
# Install system dependencies
COPY . .
RUN pip install --no-cache-dir .
RUN rm -rf /tmp/app

CMD ["uvicorn", "smart_console_adapter.main:app"]