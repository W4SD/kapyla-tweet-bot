import json
import requests
from bs4 import BeautifulSoup as BS


base_url = "https://www.palloliitto.fi"
scrape_url = "https://www.palloliitto.fi/seura/3436"

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
    print(f"found: {len(ottelut)} matches")

    return ottelut


def fetch_match_data(match_id):

    # palloliitto api url
    match_data_url = "https://www.palloliitto.fi/get-match-data"
    data = {
        'postdata': match_id,
    }
    match_data = requests.post(match_data_url, data=data)
    match_data_response = match_data.json()["call"]
    match_data_value = "ERROR"
    if match_data_response["status"] == "ok":
        # gets match data values as "type = <class 'dict'>"
        match_data_value = match_data.json()["match"]
    else:
        try:
            match_data_value = (
                f"WARNING: status: {match_data_response['status']} - "
                f"msg: {match_data_response['error_message']}")
        except KeyError:
            # this is here in case there are other status messages besided:
            # "ok" and "error"
            match_data_value = match_data_response

    return (match_data_value)


def fetch_match_details(ottelut):

    for match in ottelut:

        # splits the match_link "`base_url`/otteluseuranta/1491717" -> ["",otteluseuranta,1491717]
        match_link = base_url + match.select(".live-match-link")[0].a["data-details-href"]
        # gives the id for the match:
        match_id = match_link.split("/")[4]
        print(f"ID: {match_id}, type: {type(match_id)}")
        match_details = fetch_match_data(match_id)
        # error handling if only a string was returned -> no match_details found
        if not isinstance(match_details, str):
            match_details["is_kapyla_home"] = True if match_details["club_A_id"] == "3436" else False
            match_details["match_link"] = match_link

        # @Todo [FEAT] Venue link can be build from data -> https://www.palloliitto.fi/areena/336 -> 'venue_location_id'
        all_ottelut[match_id] = match_details
        all_ottelut.pop("lineups", None)
        print("Match details added")
        break

def scraper(json_file):

    fetch_match_details(scrape_ottelut(scrape_url))
    with open(json_file, "w+") as file:
        json.dump(all_ottelut, file)
