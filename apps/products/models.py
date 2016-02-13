from django.db import models
from datetime import date

class Product(models.Model):
	product = models.CharField(max_length=255)
	manufacturer = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	description = models.CharField(max_length=50)
	date = models.DateField()
	class Meta:
		db_table = 'products'
