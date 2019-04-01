import urllib.request
from bs4 import BeautifulSoup

# Code used to locate temperature


# Given a place from Weather.com looks for temperature
# URL should be a string
def simple_temp_reader(url_input):

    # Uses Beautiful Soup to Scrape Data
    url = url_input
    request = urllib.request.Request(url)
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Goes through store data, looking for current temp and feels like temp
    data = soup.find('div', attrs={'id': 'main-Nowcard-92c6937d-b8c3-4240-b06c-9da9a8b0d22b'})
    search_current_temp = data.find('div', attrs={'class': 'today_nowcard-temp'})
    search_feels_like_temp = data.find('span', attrs={'class': 'deg-feels'})

    # Stored as Strings, will parse to Int later
    current_temp = search_current_temp.text
    feels_like_temp = search_feels_like_temp.text
    return current_temp, feels_like_temp


print(simple_temp_reader("https://weather.com/weather/today/l/48104:4:US"))






