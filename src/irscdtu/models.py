from django.contrib import admin
from django.core.urlresolver import reverse

class Report(models.Model):
	name = models.CharField(max_lenght=100)
	email = models.CharField(max_lenght=150)
	report = models.CharField(max_lenght=500)
	
	def __str__(self):
	return self.email

