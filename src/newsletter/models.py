from django.db import models

# Create your models here.

class MailTo(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True,blank=True,default="")

    def __str__(self):
        return self.email_id
