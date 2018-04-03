from django.db import models

class MailTo(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True,blank=True,default="")
