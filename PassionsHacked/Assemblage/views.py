from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.auth.models import User
from django.core import serializers
import json
import bookingapi
from models import *

# Create your views here.

api = bookingapi.BookingAPI()

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def echo(request):
	return HttpResponse(request.GET['message'])

def register(request):
	username = request.GET['username']
	password = request.GET['password']
	try:
		user = User.objects.create_user(username = username, password = password)
	except:
		return HttpResponse("Error")
	return HttpResponse("OK")

def signin(request):
	username = request.GET['username']
	password = request.GET['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		login(request, user)
		return HttpResponse("OK")
	else:
		return HttpResponse("Error")

def signout(request):
	logout(request)
	return HttpResponse("OK")

def signtest(request):
	if not request.user.is_authenticated:
		return HttpResponse("you are not signed in")
	else:
		return HttpResponse("Welcome " + request.user.username)

def create_group(request):
	try:
		if request.user is None:
			raise ValueError("Not logged in")
 
		# create new group
		name = request.GET['name']
		destination = request.GET['destination']
		from_date = request.GET['from_date']
		to_date = request.GET['to_date']
		group = Group(name=name, destination=destination, from_date=from_date, to_date=to_date)
		group.save()

		# add currently logged in user to the particiants list
		group.participants.add(request.user)
		group.save()

		return HttpResponse(group.id)
	except:
		return HttpResponse("Error")

def add_user_to_group(request):
	try:
		group_id = request.GET['group_id']
		group = Group.objects.get(id = group_id)
		group.participants.add(request.user)
		return HttpResponse("OK")
	except:
		return HttpResponse("Error")

def get_users_from_group(request):
	#try:
		group_id = request.GET['group_id']
		group = Group.objects.get(id = group_id)
		members = group.participants.all()
		return HttpResponse(serializers.serialize('json', members))
	#except:
		return HttpResponse("Error")

def add_block_to_group(request):
	return HttpResponse("Not yet implemented")

def get_blocks_from_group(request):
	return HttpResponse("Not yet implemented")

def autocomplete(request):
	json_response = api.autocomplete(request)
	return HttpResponse(json_response, content_type="application/json")

def get_countries(request):
	json_response = api.getCountries(request)
	return HttpResponse(json_response, content_type="application/json")

