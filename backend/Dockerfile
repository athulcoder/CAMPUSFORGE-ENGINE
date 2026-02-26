FROM python:3.11-slim

# -----------------------------
# Environment
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# IMPORTANT: make /app importable
ENV PYTHONPATH=/app

WORKDIR /app

# -----------------------------
# System dependencies
# -----------------------------
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Python dependencies
# -----------------------------
COPY backend/requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Application code
# -----------------------------
COPY backend backend
# -----------------------------
# Security: non-root user
# -----------------------------
RUN useradd -m appuser \
    && chown -R appuser:appuser /app

USER appuser

# -----------------------------
# Runtime
# -----------------------------
EXPOSE 5000

CMD ["gunicorn","-b","0.0.0.0:5000","--workers","4","--threads","4","--worker-class","gthread","--timeout","60","--graceful-timeout","15","--keep-alive","5","backend.run:app"]