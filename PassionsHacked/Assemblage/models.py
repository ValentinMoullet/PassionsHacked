from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	creation_date = models.DateField(auto_now_add=True)
	

class Profile(models.Model):
	user = models.OneToOneField(User)
	groups = models.ManyToMany(Group)
	
class Hotel:
	id = models.AutoField(primary_key=True)
	creating_user = models.ForeignKey(User)
	

