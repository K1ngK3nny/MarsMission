import urllib
import urllib.request
from bs4 import BeautifulSoup

the_url = 'https://twitter.com/MarsWxReport'
the_page = urllib.request.urlopen(the_url)
soup = BeautifulSoup(the_page, 'html.parser')
mars_weather = soup.find(
    'div', {"class": "js-tweet-text-container"}).find('p').text
#print(soup.find('div', {"class": "js-tweet-text-container"}).find('p').text)
print(mars_weather)
