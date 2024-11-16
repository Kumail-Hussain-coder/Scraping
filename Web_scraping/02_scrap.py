# Only we take Paragraph from Website
# To extract the data we use bs4(BeautifulSoup4)
import requests
import bs4
import sys

sys.stdout.reconfigure(encoding = 'utf-8')
url = "https://open.spotify.com/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')

# To take the paragraph we us loop
for para in soup.find_all('p'):
    print(para.text)