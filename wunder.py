#!/usr/bin/python
''' Fetch weather information from wunder.
 - stripped down and not threaded. '''
 
# import requests
# from bs4 import BeautifulSoup
import urllib2
import json
import logging
import datetime
# import threading
import time
import keys

class Weather():
	def __init__(self, key, locn):
		self.logger = logging.getLogger(__name__)
		self.key = key
		if self.key == 'none':
			print 'No weather key, emulating.'
		self.locn = locn
		self.wunder_temperature = 0

	def wunder(self,key,locn):
		self.logger.debug("Fetching wunder temperature")
		f = urllib2.urlopen('http://api.wunderground.com/api/'+key+'/conditions/q/'+locn+'.json')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		#location = parsed_json['location']['city']
		temp_c = parsed_json['current_observation']['temp_c']
		self.logger.info("Current temperature is: %s" % (temp_c))
		f.close()
		return(str(temp_c))

if __name__ == "__main__":
	logging.basicConfig(filename='log/weather.log', filemode='w', level=logging.INFO)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+
					". Running weather class as a standalone app")

	print "Fetching wunder weather info"
	myWeather = Weather(keys.wunder, keys.locn)
	print "Temperature:", myWeather.wunder(keys.wunder,keys.locn)
	print 'Ending main.'
#	myWeather.wunder()
