from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	#add additional fields in here

	def getUserName(self):
<<<<<<< HEAD
		return self.username
=======
		return self.owner
>>>>>>> ed6f62f05803deb4e9f5c363441bb3ca7cc1a323

	# def __str__(self):
	# 	return self.username
