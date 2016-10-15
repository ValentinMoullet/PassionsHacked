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

def getParam(request, name):
	if request.method == "GET":
		qd = request.GET
	else:
		qd = request.POST
	
	return qd[name]

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def echo(request):
	message = getParam(request, 'message')
	return HttpResponse(message)

def register(request):
	username = getParam(request, 'username')
	password = getParam(request, 'password')
	firstname = getParam(request, 'firstname')
	lastname = getParam(request, 'lastname')
	try:
		user = User.objects.create_user(username = username, password = password, first_name = firstname, last_name = lastname)
		return HttpResponse(serializers.serialize('json', user))
	except:
		return HttpResponse("Error")

def signin(request):
	username = getParam(request, 'username')
	password = getParam(request, 'password')
	user = authenticate(username = username, password = password)
	if user is not None:
		login(request, user)
		return HttpResponse(serializers.serialize('json', user))
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
		name = getParam(request, 'name')
		dest_name = getParam(request, 'dest_name')
		dest_id = getParam(request, 'dest_id')
		from_date = getParam(request, 'from_date')
		to_date = getParam(request, 'to_date')
		group = Group(name=name, dest_name=dest_name, dest_id=dest_id, from_date=from_date, to_date=to_date)
		group.save()

		# add currently logged in user to the participants list
		group.participants.add(request.user)
		group.save()

		return HttpResponse(group.id)
	except:
		return HttpResponse("Error")

def get_groups_for_user(request):
	try:
		if request.user is None:
			raise ValueError("Not logged in")

		user_groups = []

		for group in Group.objects.all():
			if group.participants.filter(id = request.user.id).count() > 0:
				user_groups.append(group)

		return HttpResponse(serializers.serialize('json', user_groups))
	except:
		return HttpResponse("Error")

def add_user_to_group(request):
	try:
		group_id = getParam(request, 'group_id')
		group = Group.objects.get(id = group_id)
		user_id = getParam(request, 'user_id')

		if group.participants.filter(id = user_id).count() > 0:
			raise ValueError("Already added to the group")

		user = User.objects.get(id = user_id)
		group.participants.add(user)
		return HttpResponse("OK")
	except:
		return HttpResponse("Error")

def get_users_from_group(request):
	try:
		group_id = getParam(request, 'group_id')
		group = Group.objects.get(id = group_id)
		members = group.participants.all()
		return HttpResponse(serializers.serialize('json', members))
	except:
		return HttpResponse("Error")

def add_hotel_to_group(request):
	try:
		if request.user is None:
			raise ValueError("Not logged in")

		group_id = getParam(request, 'group_id')
		group = Group.objects.get(id = group_id)

		block_id = getParam(request, 'block_id')
		hotel_id = getParam(request, 'hotel_id')
		url = getParam(request, 'url')
		hotel_name = getParam(request, 'hotel_name')
		hotel_rating = 

		hotelInGroup = HotelInGroup(creating_user=request.user, block_id=block_id, hotel_id=hotel_id, group=group, url=url)
		hotelInGroup.save()

		return HttpResponse(hotelInGroup.id)
	except:
		return HttpResponse("Error")

def get_hotels_from_group(request):
	try:
		if request.user is None:
			raise ValueError("Not logged in")

		group_id = getParam(request, 'group_id')
		group = Group.objects.get(id = group_id)

		hotels = HotelInGroup.objects.filter(group = group)
		return HttpResponse(serializers.serialize('json', hotels))
	except:
		return HttpResponse("Error")

def vote_positive_for_hotel(request):
	try:
		vote_for_hotel_internal(request, True)
		return HttpResponse("OK")
	except:
		return HttpResponse("Error")

def vote_negative_for_hotel(request):
	try:
		vote_for_hotel_internal(request, False)
		return HttpResponse("OK")
	except:
		return HttpResponse("Error")

def vote_for_hotel_internal(request, isPositive):
	hotel_id = getParam(request, 'hotel_id')
	hotel = HotelInGroup.objects.get(id = hotel_id)

	if hotel.positive_voters.filter(id = request.user.id).count() > 0:
		raise ValueError("Already voted (positive)")
	if hotel.negative_voters.filter(id = request.user.id).count() > 0:
		raise ValueError("Already voted (negative)")

	if isPositive:
		hotel.positive_voters.add(request.user)
		hotel.total_votes += 1
	else:
		hotel.negative_voters.add(request.user)
		hotel.total_votes -= 1
	hotel.save()

def get_best_hotel_in_group(request):
    group_id = request.GET['group_id']
    group = Group.objects.get(id = group_id)

    best_hotel = HotelInGroup.objects.filter(group__id = group_id).order_by('total_votes')[0]
    print(best_hotel)

    return HttpResponse(serializers.serialize('json', best_hotel))


def autocomplete(request):
	json_response = api.autocomplete(request)
	return HttpResponse(json_response, content_type="application/json")

def get_countries(request):
	json_response = api.getCountries(request)
	return HttpResponse(json_response, content_type="application/json")

