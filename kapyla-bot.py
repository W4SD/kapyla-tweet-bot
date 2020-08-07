import conf

from pallo_scraper2 import scraper
from mongrel import Mongrel

def main():

    # Scrape
    # Scrape data from palloliitto - generates json file with match data ("matches.json"
    scraper(conf.match_json)

    # Database
    # Create database accessor
    mongrel = Mongrel(conf.db_user, conf.db_password, conf.db_address)
    # update database
    mongrel.db_updater(conf.match_json)
    # if mongrel.days_until next match = 0 tweet
    # else tweet days until next match
    # find next game

    pass

if __name__ == "__main__":
    #
    main()
