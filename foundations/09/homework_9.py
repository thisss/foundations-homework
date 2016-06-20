import time
import datetime
import dateutil.parser

'''Homework 9

We're going to make a Lil' QuakeBot!!!! Please write this code as a .py file, not a Notebook.

First, tips:
READ THROUGH THE ENTIRE ASSIGNMENT BEFORE YOU BEGIN
Be careful that you're doing all of your math with ints or floats instead of strings that look like ints or floats.
When you write your functions, you can pass either the entire dictionary to the function OR just the part you're curious about 
(e.g., when you're getting the day you could send the whole earthquake dictionary or just what's in the 'time' key.)
Writing empty functions that always return the same thing are a great way to start off. You can start saying every earthquake 
is shallow and then fill in the actual code later.
Find out what each column name in the database means by visiting http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php and 
clicking the links for each column.

PART ZERO: Overall description

Given an earthquake defined like this... '''

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

''' 
I want to be able to run

    print(eq_to_sentence(earthquake))

and get the following:

A DEPTH POWER, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE LOCATION.

So, for example, "A deep, huge 4.5 magnitude earthquake was reported Monday morning on June 22 73km WSW of Haines, Alaska".

DEPTH, POWER, MAGNITUDE, DAY, and TIME_OF_DAY should all come from separate functions. More details are in PART ONE and PART TWO. '''


def eq_to_sentence(quake):
	print("A", \
		depth_to_words(quake['depth']), \
		mag_to_words(quake['mag']), \
		"earthquake was reported", \
		day_in_words(quake['time']), \
		date_in_words(quake['time']), \
		"in the", \
		time_in_words(quake['time']), \
		earthquake['place'] \
		+ ".")


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


eq_to_sentence(earthquake)


''' 

PART THREE: Doing it in bulk

Read in the csv of the past 30 days of 1.0+ earthquke activity from http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv (tip: read_csv works with URLs!)

Because we haven't covered looping through pandas, use the following code to convert a pandas DataFrame into a list of dictionaries that you can loop through.

earthquakes_df = pd.read_csv("1.0_month.csv")
earthquakes = earthquakes_df.to_dict('records')

(If you really want to do it with pandas, it's for index, row in earthquakes_df.iterrows():)

Loop through each earthquake, printing sentence descriptions for the ones that are above or equal to 4.0 on the Richter scale.

PART FOUR: The other bits

If the earthquake is anything other than an earthquake (e.g. explosion or quarry blast), print

There was also a magnitude MAGNITUDE TYPE_OF_EVENT on DATE LOCATION.

For example,

There was also a magnitude 1.29 quarry blast on June 19 12km SE of Tehachapi, California.

with TYPE_OF_EVENT being explosion, quarry blast, etc and LOCATION being 'place' - e.g. '0km N of The Geysers, California'.
'''
