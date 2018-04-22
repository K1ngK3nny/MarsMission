
# coding: utf-8

# In[2]:


# Getting latest news from the NASA/Mars website
from bs4 import BeautifulSoup
import requests

source = requests.get(
    'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest').text

soup = BeautifulSoup(source, 'lxml')

news_title = soup.find('title')
news_p = soup.find('p')

print(news_title.text)
print(news_p.text)


# In[3]:


# Getting Mars weather info from the twitter handle
import urllib
import urllib.request
from bs4 import BeautifulSoup

the_url = 'https://twitter.com/MarsWxReport'
the_page = urllib.request.urlopen(the_url)
soup = BeautifulSoup(the_page, 'html.parser')
mars_weather = soup.find('div', {"class": "js-tweet-text-container"}).find('p').text
#print(soup.find('div', {"class": "js-tweet-text-container"}).find('p').text)
print(mars_weather)


# In[4]:


# using splinter to get the full size image url of the featured image of website
from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome', headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/'
browser.visit(url)



    
html = browser.html
    
soup = BeautifulSoup(html, 'html.parser')
    
articles = soup.find_all('article', class_='carousel_item')

    
for article in articles:
	
	featured_image = article.find('a')
	
	image = featured_image['data-link']
	featured_image_url = "https://www.jpl.nasa.gov" + image
	print(featured_image_url)


# In[15]:


# using Pandas to scrape the table of facts
from bs4 import BeautifulSoup
import pandas as pd 	
import requests
import urllib
import urllib.request

url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
print(tables)


# In[16]:


df = tables[0]
df.columns = ['Fact', 'Data']
df.set_index('Fact', inplace=True)
df


# In[17]:


html_table = df.to_html()
print(html_table)


# In[1]:


# making dictionary or hemisphere image url's
hemisphere_image_urls = [{"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
]
print(hemisphere_image_urls)
