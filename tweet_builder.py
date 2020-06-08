import random

# class TweetBuilder():
league = "LIIGA"
opponent_team = "SUKKATIIMI"
venue = "OTTELUPAIKKA"
game_time = "18.00"
game_url = "www.jeejee.fi"
kapyla_team = "käpylä"

HELLO = [
    "Jahas...",
    "GAME ON!!!",
    "Pelipäiväääääääää!",
    "Tänään fudataan!",
    "Game day",
    "Samba… Today!",
    "Aah!",
    "Ai että!",
    "Pysäyttäkää painokoneet!",
]
CONTENT = [
    f"se on {league} -sarjan pelipäivä! Tänään Käpylää vastaan asettuu {opponent_team}. "
    f"Avauspotku potkaistaan {venue}-pyhätössä klo {game_time}.",

    f"Today! Käpylä vs {opponent_team} @ {game_time}, {venue}.",
    f"Käpylä vs {opponent_team} @ {game_time}, {venue}.",
    f"{league}. {kapyla_team} vs {opponent_team} @ {game_time}, {venue}.",
    f"Käpylä is playing today against {opponent_team} in {game_time} at {venue}.",
    f"Käpylä gonna beat {opponent_team} in {game_time} at {venue} today!",

    f"Tänään nokka kohti {venue}, sillä Käpylä pelaa {opponent_team} vastaan. "
    f"\nKellonlyömä 👉 {game_time}.\n",

    f"Tänään pelataan {kapyla_team} vs {opponent_team} @ {game_time}, {venue}."

]

SPECIAL = [
    f"Mitenköhän tänään käy {opponent_team} -raukoille. Veikkaisin, "
    f"että Käpylä vie 5-0. Entä sä? Tuu {venue} -kentälle klo {game_time}.",

    f"Taas on aika {league} -sarjan! Tänään vastassa {opponent_team}. "
    f"Pilli kajahtaa {venue}-pyhätössä klo {game_time}.",

    f"Tuu tsiigaamaan kun KMPP:n pesukoneessa tänään vuorossa {opponent_team} @ {game_time}, {venue}.",

    f"Ai että! Fudis on kyllä parhaimmillaan {league} -karkeloissa! "
    f"KMPP vs {opponent_team}. Avauspotku {venue} -pyhätössä klo {game_time}.",

    f"Tekonurmi vihertää ja {kapyla_team} kohtaa {opponent_team} @ {game_time}, {venue}.",

    f"Ai HIIVAtti, {venue} porisee kuin Harperin Siideripönttö %gamedate {game_time} "
    f"kun {kapyla_team} mittaa shlongin lisäksi {opponent_team} peruskunnon!",

    f"@Gazzetta_it: Il gioco di oggi {kapyla_team} — {opponent_team}. Benvenuto!",
    f"”El clásico de {league}”: {kapyla_team} — {opponent_team} @ {venue}, {game_time}."
]

INFO = [
    f"Tsekkaa lisätiedot: {game_url}",
    f"More details {game_url}",
    f"Tsekkaa lisäinfot {game_url}.",
    f"{game_url}. #kapylamaanantai",
    f"Check the details at {game_url}.",
    f"Details: {game_url}. #kapylamaanantai",
    f"Lisäinfot: {game_url}",
    f"\nInfot haltuun 👉 {game_url}.\n#kapylamaanantai",
    f"{game_url}. #kapylamaanantai",
    f"Vähemmän oleellista #fakenews täältä: {game_url}",

]

tweet = f"{random.choice(HELLO)} {random.choice(CONTENT)} {random.choice(INFO)}"
print(f"{tweet} \n pituus: {len(tweet)}")

