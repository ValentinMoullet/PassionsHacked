import urllib2, base64, json, requests

BOOKINGCOM_API_URL = "https://hacker240:6PJfyQFLn4@distribution-xml.booking.com/json/bookings."

class BookingAPI():

	def get_countries(self, request):
		return get_response("getCountries")

	def autocomplete(self, request):
		text = request.GET['text']
		language_code = request.GET['languagecode']
		params = {}
		params['text'] = text
		params['languagecode'] = language_code
		return get_response("autocomplete", params)


def get_response(func, params={}):
	url = BOOKINGCOM_API_URL + func
	return requests.get(url, params)
