from celery import shared_task
import time

@shared_task
def heavy_process():
    time.sleep(4)
    return "Completed"