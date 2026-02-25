FROM python:3.11-slim

# -----------------------------
# System setup
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Python dependencies
# -----------------------------
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -----------------------------
# App code
# -----------------------------
COPY . .

# -----------------------------
# Security: run as non-root
# -----------------------------
RUN useradd -m appuser
USER appuser

# -----------------------------
# Expose & start
# -----------------------------
EXPOSE 5000

CMD ["gunicorn", \
     "--bind", "0.0.0.0:5000", \
     "--workers", "3", \
     "--threads", "2", \
     "--timeout", "120", \
     "run:app"]