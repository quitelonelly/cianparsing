import requests
import json

url = "https://api.cian.ru/search-offers/v2/search-offers-desktop/"
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Content-Type": "application/json",
}
params = {
    "jsonQuery": {
        "region": {"type": "terms", "value": [1]},
        "_type": "flatsale",
        "engine_version": {"type": "term" ,"value": 2},
        "page":{"type": "term", "value": 2}
    }
}

response = requests.post(url, headers=headers, json=params)
response.raise_for_status()

data = response.json()

offers = data['data']['offersSerialized']

with open("parsing.json", "w", encoding="utf-8") as f:
    f.write("[\n")
    for i, offer in enumerate(offers, start=1):
        f.write(f"  \"item{i}\": {{\n")
        f.write(f"    \"Объект\": \"{offer['formattedFullInfo']}\",\n")
        f.write(f"    \"Цена\": \"{offer['formattedFullPrice']}\",\n")
        f.write(f"    \"Общая площадь\": \"{offer['totalArea']}\",\n")
        f.write("  },\n")
    f.write("]")
