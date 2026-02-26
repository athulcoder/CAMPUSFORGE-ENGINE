import os
import io
from minio import Minio

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "minio:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minioadmin123")
MINIO_SECURE = os.getenv("MINIO_SECURE", "false").lower() == "true"
RESUME_BUCKET = os.getenv("RESUME_BUCKET", "resumes")


minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=MINIO_SECURE,
)


def ensure_bucket(bucket: str = RESUME_BUCKET):
    if not minio_client.bucket_exists(bucket):
        minio_client.make_bucket(bucket)


def upload_resume_minio(object_name: str, data: bytes, content_type: str):
    ensure_bucket()
    minio_client.put_object(
        RESUME_BUCKET,
        object_name,
        io.BytesIO(data),
        length=len(data),
        content_type=content_type,
    )

def download_from_minio(bucket: str, object_name: str) -> bytes:
    response = None
    try:
        response = minio_client.get_object(bucket, object_name)
        return response.read()
    finally:
        if response:
            response.close()
            response.release_conn()