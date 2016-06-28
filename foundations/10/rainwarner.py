import requests
response = requests.get('https://api.forecast.io/forecast/cb31c6739ae1c7377aa0c3bbc1aa9b30/40.80566,-73.96115')
forecast = response.json()

def temp_feeling(day_forecast):
    if day_forecast['temperatureMax'] > 80:
        return "hot"
    elif day_forecast['temperatureMax'] > 70:
        return "warm"
    elif day_forecast['temperatureMax'] > 60:
        return "cool"
    elif day_forecast['temperatureMax'] < 33:
        return "freezing cold"

def rain_warning(day_forecast):
    if day_forecast['precipType'] == 'rain':
        return "Bring an umbrella."

def emailer(emailtxt):
	key = '##############'
	sandbox = '##########'
	recipient = '#############'
	
	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
	request = requests.post(request_url, auth=('api', key), data={
		'from': '##############',
		'to': recipient,
		'subject': 'Your daily weather info',
		'text': emailtxt
	})

weather_message = "Right now it is " \
	+ str(forecast['currently']['temperature']) \
	+ " degrees out and " \
	+ forecast['currently']['summary'].lower() + ".\n" \
	"Today will be " + \
	temp_feeling(forecast['daily']['data'][0]) + \
	" with a high of " + \
	str(forecast['daily']['data'][0]['temperatureMax']) + \
	" and a low of " + \
	str(forecast['daily']['data'][0]['temperatureMin']) + ". " + \
	rain_warning(forecast['daily']['data'][0])

emailer(weather_message)
