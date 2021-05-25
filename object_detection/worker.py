import requests
import traceback
from PIL import Image
from celery_app import app
from object_detection.db import Job
from object_detection.model import ObjectDetector

detector = ObjectDetector()


def get_image_from_url(url):
    return Image.open(requests.get(url, stream=True).raw)

def save_output(job_id, output):
    Job(id=job_id).update(state="Done", result=output)

def set_job_state(job_id, state):
    Job(id=job_id).update(state=state)


@app.task
def run_detector(job_id, url):
    print("run_detector")
    set_job_state(job_id, "Processing")



    try:
        image =  get_image_from_url(url)
        output = detector.predict(image)

        save_output(job_id, output)

    except Exception as excp:
        traceback.print_exc()
        set_job_state(job_id, "Failed")
