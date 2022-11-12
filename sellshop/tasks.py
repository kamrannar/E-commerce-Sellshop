from celery import shared_task
from sellshop.celery import app
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Newsletter


@shared_task
def heavy_process():
    for i in Newsletter.objects.all().values_list('emails'):
        send_mail('b','a',settings.EMAIL_HOST_USER,i)
    return "Completed"

