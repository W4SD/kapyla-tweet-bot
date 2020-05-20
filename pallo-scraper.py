import requests
from bs4 import BeautifulSoup as BS


def scrape_ottelut():
    url = 'https://www.palloliitto.fi/seura/3436'
    response = requests.get(url)

    if response.status_code != requests.codes.ok:
        # page gave not 200 response so exit?
        print("lol")
        return False
    # else continue!

    page = BS(response.text, "html.parser")
    # all elements with matching class in a list
    ottelut = page.find_all('div', class_='match-row')

    print(len(ottelut))


scrape_ottelut()