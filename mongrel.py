import json
from datetime import date, datetime, timedelta, time
from pymongo import MongoClient


class Mongrel():
    """
    Single database - single collection
    all matches to the same collection
    """

    # init client
    def __init__(self, username, password, address):

        connector = "mongodb+srv://" + username + ":" + password + address
        self.Client = MongoClient(connector)
        self.db = self.Client["user"]
        # self.db = self.Client["kapyla_pallo"]
        self.collection = self.db["pelit"]
        # self.collection = self.db["all_match_data"]
        self.current_date = date.today()
        self.date_format = "%Y-%m-%d"
        self.days_until_match = None

    def __del__(self):

        self._db_cleanUp()

    # json loader
    @staticmethod
    def json_loader(json_file):

        dict_matches = None
        try:
            with open(json_file, "r") as file:
                dict_matches = json.load(file)

        except OSError:
            print("Mongrel: No json file found called: ", json_file)

        return dict_matches

    # db updater
    def db_updater(self, json_file):
        # match_data = self.json_loader("matches.json")
        match_data = self.json_loader(json_file)
        # if file_all_matches is not found bubbless as error "TypeError: 'NoneType'"
        for match in match_data:
            # single match data with ID as key
            db_key_id = match_data[match]["match_id"]
            # check in match with id exist, if not insert new, else do nothing
            self.collection.update_one({"_id": db_key_id}, {"$setOnInsert": match_data[match]}, upsert=True)

    def _convert_datetime(self, target, direction):

        converted_date = None
        try:
            if direction is "TO":
                converted_date = datetime.strptime(target, self.date_format)
            if direction is "FROM":
                converted_date = target.strftime(self.date_format)
        except AttributeError:
            print(f"Invalid direction of conversion? target = {target} - direction = {direction}")

        return converted_date

    def _add_day(self, target_date):
        # convert date to datetime object
        # date_object = datetime.strptime(target_date, self.date_format)
        date_object = self._convert_datetime(target_date, "TO")
        # add one day
        new_date = date_object + timedelta(days=1)
        # convert datetime object to string
        return self._convert_datetime(new_date, "FROM")

    def _last_game_day(self):

        return self.collection.find_one({"$query": {}, "$orderby": {"date": -1}})["date"]

    def _days_until_next_match(self):

        game_day_datetime = self._convert_datetime(self.game_day, "TO")
        today_datetime = datetime.combine(self.current_date, time(0, 0))
        # datime.timedelta object
        days_until = game_day_datetime - today_datetime
        self.days_until_match = days_until["days"]

    # find next match
    def _db_find_next_match(self) -> str:

        search_date = self.current_date.strftime(self.date_format)
        search_date = self._convert_datetime(self.current_date, "FROM")
        last_game_day = self._last_game_day()
        game_day = ""
        # finds all the games with the spesific date!
        while True:
            hits = self.collection.count_documents({"date": {"$eq": search_date}})
            if hits > 0:
                game_day = search_date
                self._days_until_next_match()
                break
            # no games in sight
            if search_date > last_game_day:
                break

            search_date = self._add_day(search_date)

        return game_day

    def db_fetch_match_data(self) -> list:

        game_day = self._db_find_next_match()
        result = []
        cursor = self.collection.find({"date": game_day})
        for game in cursor:
            result.append(game)

        return result

    # @ToDo db_match_today .. if yes find match data, if not tweet days until!

    # close client
    def _db_cleanUp(self):
        self.Client.close()
