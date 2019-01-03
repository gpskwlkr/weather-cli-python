import requests
import json
import click

'''
Keys are not working right now. You need to sign up at websites mentioned in README.md

Take a free API key there and change them in code, to make it work
'''

LOCATION_SAMPLE_API_KEY = 'c13857576c866a'
WEATHER_API_SAMPLE_KEY = '12aeec80eff2989226b8f207958d42b6'

@click.command()
@click.argument('location') 
def main(location):
    '''
    location -> str
    location - used to get weather for specified city

    Calls a function for getting weather depending on the "location" argument value
    '''
    if location == 'current':
        print(getcurrentlocation())
    else: 
        print(getlocation(location))

def getlocation(location_name):
    '''
    location_name -> str
    location_name - used for getting coordinates for specified city

    Gets latitude & longitude for specified location & sends them to "getweather" function

    return: result of "getweather" function
    '''
    url = 'https://us1.locationiq.com/v1/search.php?key={}&q={}&format=json'.format(LOCATION_SAMPLE_API_KEY, location_name)
    lat = json.loads(requests.get(url).content)[0]["lat"]
    lon = json.loads(requests.get(url).content)[0]["lon"]
    location = (lat, lon)
    return getweather(location, location_name)

def getcurrentlocation():
    '''
    If "current" was entered as city in command line, function is used to get current latitude and longitude and send them to "getweather" function

    return: result of "getweather" function
    '''
    url = 'http://ipinfo.io/json'
    res = json.loads(requests.get(url).content)
    loc = res["loc"].split(',')
    location_name = res["city"]
    return getweather(loc, location_name)

def getweather(loc, location_name):
    '''
    (list) -> float, float
    loc: (lat, lon) coordinates of city
    location_name -> str

    loc: latitude, longitude, used for getting weather
    location_name - here used just for better text formatting

    return: string with all information for specified city
    '''
    lat, lon = loc
    url = 'https://api.darksky.net/forecast/{}/{}, {}'.format(WEATHER_API_SAMPLE_KEY,lat, lon)
    weather = json.loads(requests.get(url).content)["currently"]["summary"]
    temperature = round((json.loads(requests.get(url).content)["currently"]["temperature"] - 32) * 5/9)
    return f"The weather in {location_name} is - {weather}\nTemperature is - {temperature} C"

if __name__ == "__main__":
    main()
