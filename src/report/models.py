from django.db import models

class Report(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=150)
	report = models.CharField(max_length=500)

	def __str__(self):
	       return self.email
