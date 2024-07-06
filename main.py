from bs4 import BeautifulSoup
import requests
import itertools

# Requests Web Page
url = "https://www.fox5atlanta.com/local-news"
try:
    request = requests.get(url)
except requests.ConnectionError as e:
    print("Connection Error...")
    print(e)

if request.status_code == 200:
    print("Successful acccessed the page.")
else:
    print("Oops. Something went wrong with accessing the page.")
    print(request.status_code)
    raise Exception("Couldn't connect to web page...")

# Beautiful Soup
soup = BeautifulSoup(request.content, 'html.parser')

headline_title = soup.find_all('h3', class_='title')
headline_text = soup.find_all('p', class_='dek')
headline_url = soup.find_all('a', class_='m')

# print(headline_title)
for (title, text, url) in zip(headline_title, headline_text, headline_url):
    print(title)

request.close()