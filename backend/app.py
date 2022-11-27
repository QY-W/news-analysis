#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, json
from flask_cors import CORS
import requests

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/open", methods=["GET"])
def open_door():
    return jsonify("芝麻开门！")


@app.route("/trending", methods=["GET"])
def show_list():
    # RESOURCES = [
    #     {"id": "SSNI-103", "title": "葵つかさ", "learnt": True},
    #     {"id": "JUY-349", "title": "蒂亚", "learnt": False},
    #     {"id": "MXSPS-535", "title": "麻生希", "learnt": True},
    # ]
    #    return jsonify({"status": "success", "trending": RESOURCES})
    apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
    searchContent = "trump"
    link2 = "https://content.guardianapis.com/search?&api-key=test" #"https://content.guardianapis.com/search?q=&api-key=test"
    link =  (f"https://content.guardianapis.com/search?q={searchContent}&api-key={apiKey}")
    response_API = requests.get(link2)
    #response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    results = parse_json['response']['results']
    return jsonify({"status": "success", "trendingResults": results})


if __name__ == "__main__":
    app.config["JSON_AS_ASCII"] = False
    app.run()
