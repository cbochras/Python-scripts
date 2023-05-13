import requests
from bs4 import BeautifulSoup

url = input("Enter the URL to scrape: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Scrape the desired information from the HTML here

# Save the scraped information to a file
with open("scraped_data.txt", "w") as file:
    file.write(str(soup))
