import urllib
import configparser
import requests
from bs4 import BeautifulSoup



config = configparser.ConfigParser()
config.read('config.ini')
url = config.get('general', 'url')
user_agent = config.get('general', 'user_agent')

headers = {"User-Agent": user_agent}
r = requests.get(url, timeout=1, headers=headers)
soup = BeautifulSoup(r.content, "html5lib")

print(soup)