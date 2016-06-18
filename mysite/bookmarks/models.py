from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class user(models.Model):
	username = models.CharField(max_length = 12,unique = True)
	password = models.CharField(max_length = 15)
	emailid = models.EmailField(unique = True)
	def __str__ (self):
		return self.username
