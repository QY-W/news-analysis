#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, json, request
from flask_cors import CORS
import requests

# configuration
DEBUG = True
apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


# sanity check route
@app.route("/open", methods=["GET"])
def open_door():
    return jsonify("芝麻开门！")


@app.route("/trending", methods=["GET"])
def show_list():
    # apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
    searchContent = "trump"
    link2 = "https://content.guardianapis.com/search?&api-key=test"  # "https://content.guardianapis.com/search?q=&api-key=test"
    link = f"https://content.guardianapis.com/search?q={searchContent}&api-key={apiKey}"
    response_API = requests.get(link2)
    # response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    results = parse_json["response"]["results"]
    return jsonify({"status": "success", "trendingResults": results})


@app.route("/detail", methods=["GET", "POST"])
def show_detail():
    result = ""
    if request.method == "GET":
        id = request.get_data(as_text=True)
        # result = "Flask return" + id
        result = get_detail(id)
    else:
        result = "GETMETHOD"
    return jsonify({"status": "success", "detailResults": result})


def get_detail(id):
    # apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
    newsID = "football/live/2022/dec/01/socceroos-reach-world-cup-last-16-with-famous-win-over-denmark-live-reaction"
    linkGetDetail = f"https://content.guardianapis.com/{newsID}?show-fields=bodyText&api-key={apiKey}"
    response_API = requests.get(linkGetDetail)
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    return jsonify({"status": "success", "trendingResults": parse_json["response"]})


# def process_data(data):
#     return str(data) + "Added with flask"


if __name__ == "__main__":
    app.config["JSON_AS_ASCII"] = False
    app.run()
