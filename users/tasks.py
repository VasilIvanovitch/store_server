from celery import shared_task
import uuid
from datetime import timedelta

from django import forms
from django.utils.timezone import now

from users.models import EmailVerification, User




@shared_task
def send_email_verification(user_id):    
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verivication_mail()