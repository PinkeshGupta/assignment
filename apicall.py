import requests
import json


url = "http://127.0.0.1:5000/urlaggregator"


r = requests.get(url)
with open("jsondata.json", "w") as json_file:
    json.dump(r.json(), json_file)
