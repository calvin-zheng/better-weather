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
    zip_code = input("Please enter your zip code: ")
    while (not zipcodes.is_real(zip_code)):
        print("Invalid Zip Code. Please Try Again.")
        input("Please enter your zip code: ")
    lat,long = find_lat_long(zip_code)
    forecast = darksky.get_forecast(lat, long)
    print(forecast.daily.data[0].precip_probability)
    return forecast

# Requires Valid Zip Code (string)
def find_lat_long(zip_code):
    search = SearchEngine(simple_zipcode=True)
    zipcode_data = search.by_zipcode(zip_code)
    zipcode_dict_data = zipcode_data.to_dict();
    latitude, longitude = zipcode_dict_data['lat'],zipcode_dict_data['lng']
    return latitude, longitude

# Given a place from Weather.com looks for temperature
# URL should be a string
def read_temp_with_url(url_input):

    # Uses Beautiful Soup to Scrape Data
    url = url_input
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Goes through store data, looking for current temp and feels like temp
    data_current = soup.find('div', attrs={'id': 'main-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b'})
    search_current_temp = data_current.find('div', attrs={'class': 'today_nowcard-temp'})
    search_feels_like_temp = data_current.find('span', attrs={'class': 'deg-feels'})

    # Stored as Strings, will parse to Int later
    current_temp = search_current_temp.text
    feels_like_temp = search_feels_like_temp.text

    # Look for Today's High and Lows
    # Track dp0 and dp1
    hi_lo_storage = []
    data_looking_ahead = soup.find('div', attrs={'id': 'main-LookingAhead-b39982dc-b828-42f9-9ca4-3d6686c1bb83'})
    for datum_hilo in data_looking_ahead.findAll('div', attrs={'class':'today-daypart-temp'}):
        hi_lo_storage.append(datum_hilo.text)
        print(datum_hilo.text)
        if(len(hi_lo_storage) >= 2):
            break

    return current_temp, feels_like_temp

read_forecast()

