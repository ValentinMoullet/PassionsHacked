import urllib2, base64, json

class BookingAPI():
	def getCountries(request):
		return getResponse("getCountries")

def getResponse(func):
	url = "https://distribution-xml.booking.com/json/bookings." + func
	apiUsername = "hacker240"
	apiPassword = "6PJfyQFLn4"
	request = urllib2.Request(url)
	base64string = base64.encodestring('%s:%s' % (apiUsername, apiPassword)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	result = urllib2.urlopen(request)
	jsonResponse = result.read()
	return json.loads(jsonResponse)
