import urllib2, base64, json, requests

class BookingAPI():

	BOOKINGCOM_API_URL = "https://hacker240:6PJfyQFLn4@distribution-xml.booking.com/json/bookings."

	def getCountries(request):
		return get_response("getCountries")

def get_response(func, params={}):
	url = BOOKINGCOM_API_URL + func
	return requests.get(url, params)
