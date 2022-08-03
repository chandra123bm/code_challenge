from bs4 import BeautifulSoup as bs
import requests
from geopy.geocoders import Nominatim

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_lat_lon(city_name):
  geolocator = Nominatim(user_agent='myapplication')
  location = geolocator.geocode(city_name)
  return str(location.latitude), str(location.longitude)

def get_weather_data(url, region):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")

    # store all results on this dictionary
    result = {}
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # extract latitude and longitude
    result['lat'], result['lon'] = get_lat_lon(region)


    return result

if __name__ == "__main__":
    cities = input('Enter the list of cities for the weather forecast: ')
    city_list = cities.split(',')
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
    header = "Location|Position|LocalTime|Conditions|Temperature|Humidity"
    print(header)
    for city in city_list:
      try:
        region = city
        region = region.replace(" ", "+")
        URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
        URL += f"+{region}"
        data = get_weather_data(URL, region)
        print('{}|{},{}|{}|{}|{}|{}'.format(data["region"],data["lat"],data["lon"],data["dayhour"],data['weather_now'],data['temp_now'],data["humidity"]))
      except:
        pass