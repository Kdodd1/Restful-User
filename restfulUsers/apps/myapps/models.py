from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 2:
			errors["first_name"] = "*First name must contain at least 3 characters"
		elif not NAME_REGEX.match(postData['first_name']):
			errors["first_name"] = "*First name can't contain special characters or numbers"

		if len(postData['last_name']) <2:
			errors["last_name"] = "*Last name must contain at least 3 characters"
		elif not NAME_REGEX.match(postData['last_name']):
			errors["last_name"] = "*Last name can't contain special characters or numbers"
		if not EMAIL_REGEX.match(postData['email']):
			errors["emails"] = "*Not a valid email"
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	objects = UserManager()

