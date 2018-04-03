from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.
def send_email(request,subject,message):
    q = models.MailTo.objects.all()
    for p in q:
        try:
            send_mail(subject, message, from_email, p.email_id)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
