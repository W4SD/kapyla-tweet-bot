import requests
from bs4 import BeautifulSoup as BS

base_url = "https://www.palloliitto.fi"
scrape_url = "https://www.palloliitto.fi/seura/3436"
all_ottelut = {}

def scrape_ottelut(url):

    response = requests.get(url)

    if response.status_code != requests.codes.ok:
        # page gave not 200 response so exit?
        print("lol")
        return False
    # else continue!

    page = BS(response.text, "html.parser")
    # all elements with matching class in a bs4.element.ResultSet
    ottelut = page.find_all("div", class_="match-row")

    return ottelut


def separate_ottelut(ottelut):


    for match in ottelut:
        match_details = {}

        match_details["sarja"] = match.find("div", class_="category-column").get_text()
        match_details["koti"] = (
            match.select(".home-team-wrapper .team-name")[0].a.get_text()
        )
        match_details["vieras"] = (
            match.select(".visiting-team-wrapper .team-name")[0].a.get_text()
        )
        # ToDo [FEAT] Need to convert this time stamp to datetime-object ?
        # ToDo [BUG] start_time also has line break and lots of empty space!
        match_details["start_time"] = (
            match.find("div", class_="match-time-wrapper").get_text()
        )
        match_link = match.select(".live-match-link")[0].a["data-details-href"]
        # splits the match_link "/otteluseuranta/1491717" -> ["",otteluseuranta,1491717]
        match_id = match_link.split("/")[2]
        match_details["match_link"] = base_url + match_link

        all_ottelut[match_id] = match_details


separate_ottelut(scrape_ottelut(scrape_url))
print(all_ottelut)