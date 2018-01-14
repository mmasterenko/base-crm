from celery import Celery
from django.core.mail import send_mail


app = Celery('main', backend='redis://localhost/2', broker='redis://localhost/1')


@app.task
def add(x, y):
    return x + y


@app.task
def send_email(subject, message, from_email, recipients):
    result = send_mail(subject=subject,
                       message=message,
                       from_email=from_email,
                       recipient_list=recipients)
    return result
