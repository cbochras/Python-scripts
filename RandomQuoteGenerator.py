import requests
from bs4 import BeautifulSoup
import random

# don't forget to install the library : pip install beautifulsoup4
# url of the website to scrape
url = 'https://www.brainyquote.com/topics/inspirational-quotes'

# get the HTML content of the website
response = requests.get(url)
html = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find all the quote elements on the page
quote_elements = soup.find_all('a', {'title': 'view quote'})

# extract the text of each quote element
quotes = [element.text for element in quote_elements]

# select a random quote from the list
quote = random.choice(quotes)

# print the quote
print(quote)
