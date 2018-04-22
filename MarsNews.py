from bs4 import BeautifulSoup
import requests

source = requests.get(
    'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest').text

soup = BeautifulSoup(source, 'lxml')

news_title = soup.find('title')
news_p = soup.find('p')

print(news_title)
print(news_p)
