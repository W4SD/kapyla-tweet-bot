import requests
from bs4 import BeautifulSoup as BS

base_url = "https://www.palloliitto.fi"
scrape_url = "https://www.palloliitto.fi/seura/3436"
crest = "https://ucdn.torneopal.fi/logo/palloliitto/3436x.png"
match_data_url = "https://www.palloliitto.fi/get-match-data"
all_ottelut = {}

def scrape_ottelut(url):

    response = requests.get(url)

    if response.status_code != requests.codes.ok:
        # page gave not 200 response so exit?
        print("Failed to get match data")
        return False
    # else continue!

    page = BS(response.text, "html.parser")
    # all elements with matching class in a bs4.element.ResultSet
    ottelut = page.find_all("div", class_="match-row")

    return ottelut

def scrape_venue_details(url):

    # url example (https://www.palloliitto.fi/otteluseuranta/1491645)
    # venue details are fetched with ajax script from the site
    # fetch("https://www.palloliitto.fi/get-match-data", {
    #   "headers": {
    #     "accept": "application/json, text/javascript, */*; q=0.01",
    #     "accept-language": "en-US,en;q=0.9,fi;q=0.8",
    #     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "sec-fetch-dest": "empty",
    #     "sec-fetch-mode": "cors",
    #     "sec-fetch-site": "same-origin",
    #     "x-requested-with": "XMLHttpRequest"
    #   },
    #   "referrer": "https://www.palloliitto.fi/otteluseuranta/1491645",
    #   "referrerPolicy": "no-referrer-when-downgrade",
    #   "body": "postdata=1491645",
    #   "method": "POST",
    #   "mode": "cors",
    #   "credentials": "include"
    # });

    # curl
    # 'https://www.palloliitto.fi/get-match-data' \
    # - H
    # 'authority: www.palloliitto.fi' \
    # - H
    # 'accept: application/json, text/javascript, */*; q=0.01' \
    # - H
    # 'x-requested-with: XMLHttpRequest' \
    # - H
    # 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' \
    # - H
    # 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
    # - H
    # 'origin: https://www.palloliitto.fi' \
    # - H
    # 'sec-fetch-site: same-origin' \
    # - H
    # 'sec-fetch-mode: cors' \
    # - H
    # 'sec-fetch-dest: empty' \
    # - H
    # 'referer: https://www.palloliitto.fi/otteluseuranta/1491645' \
    # - H
    # 'accept-language: en-US,en;q=0.9,fi;q=0.8' \
    # - H
    # 'cookie: __cfduid=d421efc69e7fcea1324540618536cccb71589645357; has_js=1' \
    # - -data - raw
    # 'postdata=1491645' \
    # - -compressed


    venue_site = requests.get(url)
    # venue name
    # venue address
    #

    if venue_site.status_code != requests.codes.ok:
        # page gave not 200 response so exit?
        print("Failed to get venue data")
        return False

    page = BS(venue_site.text, "html.parser")

    venue_url = page.find("div", class_="match-info")
    print(venue_url)


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
        match_link = base_url + match.select(".live-match-link")[0].a["data-details-href"]
        # splits the match_link "base_url/otteluseuranta/1491717" -> ["",otteluseuranta,1491717]
        match_id = match_link.split("/")[2]
        home_crest_url = (
            match.select(".home-team-wrapper")[0].img["src"]
        )
        # check if kapyla is playing home field by comparing crest data
        match_details["is_kapyla_home"] = True if crest == home_crest_url else False
        match_details["match_link"] = match_link
        venue_details = scrape_venue_details(match_link)
        # match_details["venue"] =

        all_ottelut[match_id] = match_details

test = "https://www.palloliitto.fi/otteluseuranta/1491645"

scrape_venue_details(test)
# separate_ottelut(scrape_ottelut(scrape_url))
# print(all_ottelut)