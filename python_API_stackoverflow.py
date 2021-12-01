import requests
import json
import webbrowser
from datetime import datetime, timedelta

timeBefore = timedelta(days=1)
myTime = datetime.today() - timeBefore


param = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(myTime.timestamp()),
    "tagged" : "python",
    "min" : 4
    }

link = requests.get("https://api.stackexchange.com/2.3/questions/", param)

try:
    questions = link.json()
except json.decoder.JSONDecodeError:
    print("invalid format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])