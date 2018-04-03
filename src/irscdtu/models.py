from django.contrib import admin
from django.core.urlresolver import reverse
from django.db import models

class MailTo(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(unique=True,blank=True,default="")



class Report(models.Model):
	name = models.CharField(max_lenght=100)
	email = models.CharField(max_lenght=150)
	report = models.CharField(max_lenght=500)

	def __str__(self):
	return self.email
