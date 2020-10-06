import requests
import config

headers = {
    "Authorization": "Bearer " + config.api_key
}
url = "https://api.yelp.com/v3/businesses/search"

params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses
         if business["rating"] > 4.5]
print(names)
