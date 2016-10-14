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
		group_id = request.POST['group_id']

		if 'user_id' in request.POST:
			user_id = request.POST['user_id']
			user = User.objects.get(id = user_id)
		else:
			user = request.user

		group = Group.objects.get(id = group_id)
		group.participants.add(user)
		return HttpResponse("OK")
	except:
		return HttpResponse("Error")

def get_users_from_group(request):
	try:
		group_id = request.GET['group_id']
		group = Group.objects.get(id = group_id)
		members = group.participants.all()
		return HttpResponse(serializers.serialize('json', members))
	except:
		return HttpResponse("Error")

def add_hotel_to_group(request):
	try:
		if request.user is None:
			raise ValueError("Not logged in")

		group_id = request.GET['group_id']
		group = Group.objects.get(id = group_id)

		block_id = request.GET['block_id']
		hotel_id = request.GET['hotel_id']
		url = request.GET['url']

		hotelInGroup = HotelInGroup(creating_user=request.user, block_id=block_id, hotel_id=hotel_id, group=group, url=url, positive_votes=0, negative_votes=0	)
		hotelInGroup.save()

		return HttpResponse(hotelInGroup.id)
	except:
		return HttpResponse("Error")

def get_hotels_from_group(request):
	try:
		if request.user is None:
			raise ValueError("Not logged in")

		group_id = request.GET['group_id']
		group = Group.objects.get(id = group_id)

		hotels = HotelInGroup.objects.filter(group = group)
		return HttpResponse(serializers.serialize('json', hotels))
	except:
		return HttpResponse("Error")

def autocomplete(request):
	json_response = api.autocomplete(request)
	return HttpResponse(json_response, content_type="application/json")

def get_countries(request):
	json_response = api.getCountries(request)
	return HttpResponse(json_response, content_type="application/json")

def vote_positive_for_hotel(request):

	return HttpResponse()

def vote_negative_for_hotel(request):

	return HttpResponse()

def get_ranked_hotels_in_group(request):
	group_id = request.GET['group_id']
	group = Group.objects.get(id = group_id)

	# TODO: modify, not working
	hotels = HotelInGroup.objects.filter(group__id = group_id).order_by('-negative_votes + positive_votes').all()
	print(hotels)

	return HttpResponse()
