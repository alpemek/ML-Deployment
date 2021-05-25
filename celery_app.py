from celery import Celery
import os

class Config:
    enable_utc = True
    timezone = 'Europe/London'
    broker_url = os.environ.get("BROKER_URL")
    result_backend = os.environ.get("RESULT_BACKEND")
    imports = ("object_detection.worker")
    worker_concurrency = 1

app = Celery()

app.config_from_object(Config)