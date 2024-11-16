# If you Scrape the data from any website first you get here the whole data in this vs windows
# let start

# These are the library to help that you get the data
import requests
import bs4
import sys

# The sys library is used to match the character then it take if it is not match it ignore
sys.stdout.reconfigure(encoding = 'utf-8') 

url = "https://open.spotify.com/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
print(soup.prettify())