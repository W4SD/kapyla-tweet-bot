import random
import json

class TweetBuilder():

    def __init__(self, game_data):

        self.league = game_data["category_name"]
        self.opponent_team = self._get_opponent_team(game_data)
        self.kapyla_team = self._get_kapyla_team(game_data)
        self.game_venue = game_data["venue_name"]
        self.game_time = game_data["time"]
        self.game_url = game_data["match_link"]

        self.HELLO = [
            "Jahas...",
            "GAME ON!!!",
            "Pelipäiväääääääää!",
            "Tänään fudataan!",
            "Game day",
            "Samba… Today!",
            "Aah!",
            "Ai että!",
            "Pysäyttäkää painokoneet!",
            "Today!",
            "Tänään!",
            "Tänään pelataan",
        ]

        self.CONTENT = [
            f"Se on '{self.league}' -sarjan pelipäivä! Tänään Käpylää vastaan asettuu {self.opponent_team}. "
            f"Avauspotku potkaistaan {self.game_venue}-pyhätössä klo {self.game_time}.",

            f"Käpylä vs {self.opponent_team} @ {self.game_time}, {self.game_venue}.",
            f"Käpylä vs {self.opponent_team} @ {self.game_time}, {self.game_venue}.",
            f"{self.league}. {self.kapyla_team} vs {self.opponent_team} @ {self.game_time}, {self.game_venue}.",
            f"Käpylä is playing today against {self.opponent_team} in {self.game_time} at {self.game_venue}.",
            f"Käpylä gonna beat {self.opponent_team} in {self.game_time} at {self.game_venue} today!",

            f"Nokka kohti {self.game_venue}, sillä Käpylä pelaa {self.opponent_team} vastaan. "
            f"\nKellonlyömä 👉 {self.game_time}.\n",

            f"{self.kapyla_team} vs {self.opponent_team} @ {self.game_time}, {self.game_venue}."

        ]

        self.SPECIAL = [
            f"Mitenköhän tänään käy {self.opponent_team} -raukoille. Veikkaisin, "
            f"että Käpylä vie 5-0. Entä sä? Tuu {self.game_venue} -kentälle klo {self.game_time}.",

            f"Taas on aika {self.league} -sarjan! Tänään vastassa {self.opponent_team}. "
            f"Pilli kajahtaa {self.game_venue}-pyhätössä klo {self.game_time}.",

            f"Tuu tsiigaamaan kun KMPP:n pesukoneessa tänään vuorossa {self.opponent_team} @ {self.game_time}, {self.game_venue}.",

            f"Ai että! Fudis on kyllä parhaimmillaan {self.league} -karkeloissa! "
            f"KMPP vs {self.opponent_team}. Avauspotku {self.game_venue} -pyhätössä klo {self.game_time}.",

            f"Tekonurmi vihertää ja {self.kapyla_team} kohtaa {self.opponent_team} @ {self.game_time}, {self.game_venue}.",

            f"Ai HIIVAtti, {self.game_venue} porisee kuin Harperin Siideripönttö %gamedate {self.game_time} "
            f"kun {self.kapyla_team} mittaa shlongin lisäksi {self.opponent_team} peruskunnon!",

            f"@Gazzetta_it: Il gioco di oggi {self.kapyla_team} — {self.opponent_team}. Benvenuto!",
            f"”El clásico de {self.league}”: {self.kapyla_team} — {self.opponent_team} @ {self.game_venue}, {self.game_time}."
        ]

        self.INFO = [
            f"Tsekkaa lisätiedot: {self.game_url}",
            f"More details {self.game_url}",
            f"Tsekkaa lisäinfot {self.game_url}.",
            f"{self.game_url}. #kapylamaanantai",
            f"Check the details at {self.game_url}.",
            f"Details: {self.game_url}. #kapylamaanantai",
            f"Lisäinfot: {self.game_url}",
            f"\nInfot haltuun 👉 {self.game_url}.\n#kapylamaanantai",
            f"{self.game_url}. #kapylamaanantai",
            f"Vähemmän oleellista #fakenews täältä: {self.game_url}",

        ]



    def _get_opponent_team(self, game_data):

        oppo_team = ""
        if game_data["is_kapyla_home"]:
            oppo_team = game_data["club_B_name"]
        else:
            oppo_team = game_data["club_A_name"]

        return oppo_team

    def _get_kapyla_team(self, game_data):

        kapyla_team = ""
        if game_data["is_kapyla_home"]:
            kapyla_team = game_data["club_A_name"]
        else:
            kapyla_team = game_data["club_B_name"]

        return kapyla_team

    def generate_tweet(self):

        # crude way to have weighted choice
        # @ToDo rancom.choices weighted choice ?
        tweet_type = [1, 1, 1, 1, 2]
        tweet = ""
        #normal tweet -> [HELLO][CONTENT][INFO]
        if random.choice(tweet_type) == 1:
            tweet = (
                f"{random.choice(self.HELLO)} {random.choice(self.CONTENT)} {random.choice(self.INFO)}"
            )
        # special tweet -> [SPECIAL][INFO]
        else:
            tweet = f"{random.choice(self.SPECIAL)} {random.choice(self.INFO)}"

        return tweet

# TWEET GENERATOR TESTER!
# URL in TWEETS ARE ALWAYS 23 characters by TWITTER MADE RULES!
with open("example_match_data.json", 'r') as f:
    data = json.load(f)

tweet_test = TweetBuilder(data["match"])
the_tweet = tweet_test.generate_tweet()

print(f"{the_tweet} \n Pituus: {len(the_tweet)}")