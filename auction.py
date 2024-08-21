import requests
import pprint
import os

url = "https://api.hypixel.net/skyblock/auctions"

response = requests.get(url)
data = response.json()

if not data["success"]:
    print("Failure")
    os.abort()

print(f"Total Pages: {data['totalPages']}\nTotal Auctions: {data['totalAuctions']}\nPage: {data['page']}")

reforges = []

for item in data["auctions"]:
    if "Withered" in item["item_name"]:
        pprint.pprint(item)
        break

import json

class Auction:
    class Item:
        def __init__(self, data) -> None:
            self.auctioneer = data["auctioneer"]
            self.item_lore = data["item_lore"]
            self.item_name = data["item_name"]
            self.starting_bid = data["starting_bid"]
            self.tier = data["tier"]
            self.uuid = data["uuid"]
            self.craft_cost = {"cost": 0, "modifiers": {}, "items": {}}

    class Reforge:
        def __init__(self) -> None:
            self.reforges = json.load(open("NotEnoughUpdates-REPO/constants/reforges.json"))
            self.reforge_stones = json.load("NotEnoughUpdates-REPO/constants/reforgestones.json")
        @classmethod
        def strip(item):
            

    def __init__(self) -> None:
        self.url = "https://api.hypixel.net/skyblock/auctions"

        

    def get_auctions(self):
        response = requests.get(url)
        return response.json()

