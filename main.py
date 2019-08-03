import urllib
import configparser

config = configparser.SafeConfigParser()
config.read('config.ini')
url = config.get('general', 'url')

print(url)