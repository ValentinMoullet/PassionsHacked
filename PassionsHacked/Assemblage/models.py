from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=100)
	destination = models.CharField(max_length=100)
	creation_date = models.DateField(auto_now_add=True)
	from_date = models.DateField()
	to_date = models.DateField()
	participants = models.ManyToManyField(User)

class HotelInGroup(models.Model):
	creating_user = models.ForeignKey(User, related_name='%(class)s_requests_created')
	block_id = models.CharField(max_length=100)
	hotel_id = models.CharField(max_length=100)
	url = models.CharField(max_length=200)
	group = models.ForeignKey(Group)
	positive_voters = models.ManyToManyField(User, related_name='%(class)s_positive_voters')
	negative_voters = models.ManyToManyField(User, related_name='%(class)s_negative_voters')
	total_votes = models.IntegerField()

