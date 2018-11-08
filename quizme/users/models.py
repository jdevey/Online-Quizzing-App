from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	#add additional fields in here
	games = []

	def getUserName():
		return self.username

	#def __str__(self):
	#	return self.email
