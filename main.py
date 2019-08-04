import urllib
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
url = config.get('general', 'url')

print(url)