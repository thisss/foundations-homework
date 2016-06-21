import time
import dateutil.parser
import pandas as pd

earthquake = {
	'rms': '1.85',
	'updated': '2014-06-11T05:22:21.596Z',
	'type': 'earthquake',
	'magType': 'mwp',
	'longitude': '-136.6561',
	'gap': '48',
	'depth': '10',
	'dmin': '0.811',
	'mag': '5.7',
	'time': '2014-06-04T11:58:58.200Z',
	'latitude': '59.0001',
	'place': '73km WSW of Haines, Alaska',
	'net': 'us',
	'nst': '',
	'id': 'usc000rauc'}


def eq_to_sentence(quake):
	print("A", \
		depth_to_words(quake['depth']), \
		mag_to_words(quake['mag']), \
		"earthquake was reported", \
		day_in_words(quake['time']), \
		"on", \
		date_in_words(quake['time']), \
		"in the", \
		time_in_words(quake['time']), \
		earthquake['place'] \
		+ ".")

def ex_to_sentence(explosion):
	print("There was also a magnitude", explosion['mag'], explosion['type'], "on", date_in_words(explosion['time']), explosion['place'] + ".")


def depth_to_words(depth):
	if int(depth) > 300:
		return "deep"
	if int(depth) > 70:
		return "intermediate"
	if int(depth) < 70:
		return "shallow"
	else:
		return " "

def mag_to_words(mag):
	if float(mag) > 8 :
		return "ground breaking strong"
	elif float(mag) > 7:
		return "great"
	elif float(mag) > 6: 
		return "strong"
	elif float(mag) > 5:
		return "moderate"
	elif float(mag) > 4: 
		return "light"
	else:
		return "minor"

def day_in_words(timestring): 
	yourdate = dateutil.parser.parse(timestring)
	return yourdate.strftime("%A")

def date_in_words(timestring):
	yourdate = dateutil.parser.parse(timestring)
	return yourdate.strftime("%B %d")

def time_in_words(datestring):
	yourdate = dateutil.parser.parse(datestring)
	weekday = yourdate.strftime("%A")
	time = yourdate.strftime("%H:%M")
	if time < '06:00' :
		return "night"
	if time < '12:00': 
		return "morning"
	if time < '18:00':
		return "afternoon"
	if time < '24:00': 
		return "evening" 
	else: 
		return "invalid time"


earthquakes_df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")
earthquakes = earthquakes_df.to_dict('records')

for earthquake in earthquakes: 
	if earthquake['type'] != 'earthquake':
		ex_to_sentence(earthquake)
	if earthquake['mag'] > 4:
		eq_to_sentence(earthquake)
