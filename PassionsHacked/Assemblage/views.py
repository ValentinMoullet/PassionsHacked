from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
import requests

from django.contrib.auth.models import User
import json
import bookingapi

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

def autocomplete(request):
	json_response = api.autocomplete(request)
	return HttpResponse(json_response, content_type="application/json")

def get_countries(request):
	json_response = api.getCountries(request)
	return HttpResponse(json_response, content_type="application/json")

def add_hotel_in_group(request):

	return HttpResponse()

def get_hotels_in_group(request):

	return HttpResponse()

def positive_vote_for_hotel(request):

	return HttpResponse()

def positive_vote_for_hotel(request):

	return HttpResponse()

def get_best_hotel_in_group(request):

	return HttpResponse()
