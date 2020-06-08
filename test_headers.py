import requests

headers = {
    # 'authority': 'www.palloliitto.fi',
    # 'accept': 'application/json, text/javascript, */*; q=0.01',
    # 'x-requested-with': 'XMLHttpRequest',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'origin': 'https://www.palloliitto.fi',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-dest': 'empty',
    # 'referer': 'https://www.palloliitto.fi/otteluseuranta/1491645',
    # 'accept-language': 'en-US,en;q=0.9,fi;q=0.8',
    # 'cookie': '__cfduid=d421efc69e7fcea1324540618536cccb71589645357; has_js=1',
}

data = {
  'postdata': '1507270'
}

response = requests.post('https://www.palloliitto.fi/get-match-data', data=data)

print(response.text)