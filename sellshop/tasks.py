from celery import shared_task
from sellshop.celery import app
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Newsletter
import time
from sellshop.celery import app
from django.core.mail import EmailMultiAlternatives
from product.models import Product_version
products=Product_version.objects.all()

@app.task
def periodic_test_task(bind=True):
    # time.sleep(5)
    for i in Newsletter.objects.all().values_list('email'):
            subject, from_email, to = 'hello', settings.EMAIL_HOST_USER, i
            text_content = 'This is an important message.'
            html_content=''
            
            for producte in products:
                html_content +='<div>Here are the products you missed</div><div class="product-img"></div><div class="col-xs-12 col-md-8" ><div class="list-text"><h3>'+producte.product.title+'</h3></a><h5>$ '+str(producte.discount_price)+'</h5><p>'+producte.text+'</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, i)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    return "Completed"
