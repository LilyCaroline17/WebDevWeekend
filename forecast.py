import requests
from bs4 import BeautifulSoup


def printForecast():
    page = requests.get("https://forecast.weather.gov/MapClick.php?site=PBZ&lat=40.4392&lon=-79.9767#.YZFg0i1h1QI")
    soup = BeautifulSoup(page.content, 'html.parser')
    lst = soup.find_all(class_="forecast-tombstone")
    for item in lst:
        day = item.find(class_="period-name").get_text()
        description = item.find(class_="short-desc").get_text()
        temp = item.find(class_="temp").get_text()
        print(f'(day): (description) with (temp)')

printForecast()
