from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
	STATUS = (
			('BOUGHT', 'BOUGHT'),
			('NOT AVAILABLE', 'NOT AVAILABLE'),
			('PENDING', 'PENDING'),
			)
	user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	name=models.CharField(max_length=200, null=True,default='demo item')
	quantity=models.CharField(max_length=200, null=True,default='00kg')
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	date_created=models.DateTimeField(auto_now_add=True, null =True)

	def __str__(self):
		return self.name
