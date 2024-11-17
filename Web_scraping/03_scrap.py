import requests
import bs4
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://open.spotify.com/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')


# We extract the link from this url or website
for links in soup.find_all('a'):
    link = links.get('href')
    if link[0:3] == 'art' and link != "#":
        print("https://open.spotify.com/" + link[0:len(link)])
    else:
        print("https://open.spotify.com/" + link)