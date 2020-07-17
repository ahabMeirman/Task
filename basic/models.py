from django.db import models

# Create your models here.

class Company(models.Model):

	rank = models.PositiveIntegerField()
	employer = models.CharField(max_length = 50)
	employees = models.PositiveIntegerField()
	salary = models.PositiveIntegerField()

	def __str__(self):
		return self.employer
