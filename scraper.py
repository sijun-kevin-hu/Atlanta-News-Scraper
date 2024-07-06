from bs4 import BeautifulSoup
import requests


def scrape():  
    url = "https://www.fox5atlanta.com/tag/us/ga/atlanta"
    # Requests Web Page
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

    headlines = []

    for i in range(len(headline_text)):
        headline = f"Headline {i+1}: {headline_title[i].get_text().strip()}\n{headline_text[i].get_text().strip()}"
        headlines.append(headline)

    for headline in headlines:
        print(headline)
        print()

    request.close()

    return headlines

