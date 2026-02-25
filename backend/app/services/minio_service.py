# app/services/minio_service.py
from minio import Minio
from flask import current_app
import io

def minio_client():
    return Minio(
        current_app.config["MINIO_ENDPOINT"],
        access_key=current_app.config["MINIO_ACCESS_KEY"],
        secret_key=current_app.config["MINIO_SECRET_KEY"],
        secure=current_app.config["MINIO_SECURE"],
    )

def upload_to_minio(object_name: str, data: bytes, content_type: str):
    client = minio_client()
    bucket = current_app.config["RESUME_BUCKET"]

    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)

    client.put_object(
        bucket,
        object_name,
        io.BytesIO(data),
        length=len(data),
        content_type=content_type,
    )