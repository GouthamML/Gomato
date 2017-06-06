import json
import httplib2

import sys
import codecs

foursquare_client_id = 'A5SLLJZFCW5YJH1OFDSJ2ANDKBGFQIJZGENOEZTMITSY5LJS'
foursquare_client_secret = 'AAT153KQCIEG3CHYX5JLVMCZ5UBQH4FCVA0LXSVKAYJFBNFI'
google_api_key = 'AIzaSyAox4Mjj81wNdY-RQuYB496vJ8j0ilu80o'

def getGeocodeLocation(inputString):
    #Replace Spaces with '+' in URL
		locationString = inputString.replace(" ", "+")
		url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_api_key))
    # url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))
		h = httplib2.Http()
    		result = json.loads(h.request(url,'GET')[1])
    #print response
    		latitude = result['results'][0]['geometry']['location']['lat']
    		longitude = result['results'][0]['geometry']['location']['lng']
    		return (latitude,longitude)

def findARestaurant(mealType, location):
		latitude, longitude = getGeocodeLocation(location)
    		url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s'%(foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
    		h = httplib2.Http()
    		result = json.loads(h.request(url,'GET')[1])
    		return result


# bang = getGeocodeLocation("Banglore karnataka")
