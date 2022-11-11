import requests

res = requests.get("https://developer.foursquare.com/docs/legacy-venue-categories")
print(res.text)