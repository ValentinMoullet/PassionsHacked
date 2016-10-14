import urllib2, base64, json, requests

BOOKINGCOM_API_URL = "https://hacker240:6PJfyQFLn4@distribution-xml.booking.com/json/bookings."

class BookingAPI():

	def get_countries(self, request):
		language_code = 'en'
		params = {}
		params['languagecode'] = language_code
		return get_response("getCountries", params)

	def autocomplete(self, request):
		text = request.GET['text']
		language_code = 'en'
		params = {}
		params['text'] = text
		params['languagecode'] = language_code
		return get_response("autocomplete", params)


def get_response(func, params={}):
	url = BOOKINGCOM_API_URL + func
	return requests.get(url, params)
