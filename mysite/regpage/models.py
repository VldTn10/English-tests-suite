from django.db import models
from django.utils import timezone

class regPage(models.Model):
	fisName = models.CharField('fisName', max_length=200, blank = False)
	secName = models.CharField('secName', max_length=200, blank = True)
	login = models.CharField(max_length=200, blank = True)
	password = models.CharField(max_length=18, blank = True)
	email = models.EmailField('Email', blank = False)
	phone_number = models.CharField('phoneNumber', max_length = 15)

	def __str__(self):
		print(fisName)
# Create your models here.
