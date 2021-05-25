from celery_app import app
from object_detection.db import Job

run_detector = app.signature(
    'object_detection.worker.run_detector')


def start_job(url):
    job = Job(source=str(url))
    job.save()
    
    run_detector.delay(str(job.id), url)

    return job.to_dict()

def get_jobs():
    return [job.to_dict() for job in Job.objects()]

def get_job(job_id):
    return Job.objects(id=job_id).first().to_dict()
