import conf

from pallo_scraper2 import scraper
from mongrel import Mongrel
from tweet_builder import TweetBuilder
from tweetter import Tweetter

def main():

    # Scrape
    # Scrape data from palloliitto - generates json file with match data ("matches.json"
    scraper(conf.match_json)

    # Database
    # Create database accessor
    mongrel = Mongrel(conf.db_user, conf.db_password, conf.db_address)
    # update database
    mongrel.db_updater(conf.match_json)
    # find next match day
    mongrel.db_find_next_match()
    # generate tweet
    TweetBot = Tweetter()
    tweet = ""
    if mongrel.days_until_match is 0:
        game_data = mongrel.db_fetch_match_data()
        for game in game_data:
            TB = TweetBuilder(game)
            tweet = TB.generate_tweet()
            del TB
            # tweet for every loop!
            print(tweet)

    # else tweet days until next match
    else:
        # @ToDo rng tekstit tälle ja TweetBuilder luokan päivitys
        tweet = f"Enää {mongrel.days_until_match} päivää jäljellä seuraavaan matsiin!"
        print(tweet)

    print("Daily tweets done!")


if __name__ == "__main__":
    #
    main()
