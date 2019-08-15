import urllib.request
from bs4 import BeautifulSoup
from uszipcode import SearchEngine
import zipcodes
import config
from darksky.api import DarkSky
from darksky.types import languages, units, weather


darksky = DarkSky(config.api_key)

#User Input Zip Code, Uses Dark Sky API
def read_forecast():
    #print("hello")
    zip_code = input("Please enter your zip code: ")
    while (not zipcodes.is_real(zip_code)):
        print("Invalid Zip Code. Please Try Again.")
        zip_code = input("Please enter your zip code: ")
    lat,long = find_lat_long(zip_code)
    forecast = darksky.get_forecast(lat, long)
    return forecast

# Requires Valid Zip Code (string)
def find_lat_long(zip_code):
    search = SearchEngine()
    zipcode_data = search.by_zipcode(zip_code)
    zipcode_dict_data = zipcode_data.to_dict()
    latitude, longitude = zipcode_dict_data['lat'],zipcode_dict_data['lng']
    return latitude, longitude
