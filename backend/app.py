#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, json, request, current_app
from flask_cors import CORS
import requests
from nltk.corpus import stopwords
from wordcloud import WordCloud
import io
import os
import base64
import matplotlib
from collections import Counter

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# configuration
DEBUG = True
apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
# instantiate the app
# app = Flask(__name__)
app = Flask(__name__)


app.config.from_object(__name__)
# enable CORS
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PATH_TO_SAVE = os.path.join(BASE_DIR, "frontend/src/assets")


# def save_img(img):
#     # MEDIA = current_app.config["BASE_DIR"]
#     filename = "ssss"
#     img_path = os.path.join(PATH_TO_SAVE, filename)  # 将路径和文件名拼接在一起，方便保存文件
#     img.save(img_path)  # 将图片对象保存到 本地
#     return filename


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
    if request.method == "POST":
        # content
        id = request.get_data(as_text=True)
        result = get_detail(id)
        content = result["fields"]["bodyText"]

        # word cloud
        cloudFileName = save_wordcloud(content)

        # word count
        wordCount = get_wordCount(content)
        return jsonify(
            {
                "status": "success",
                "detailResults": result,
                "wordcloud": cloudFileName,
                "wordcount": wordCount,
            }
        )


def get_detail(id):
    # apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
    # newsID = "football/live/2022/dec/01/socceroos-reach-world-cup-last-16-with-famous-win-over-denmark-live-reaction"
    # linkGetDetail = f"https://content.guardianapis.com/{id}?show-fields=bodyText&api-key={apiKey}"
    apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
    # newsID = "football/live/2022/dec/01/socceroos-reach-world-cup-last-16-with-famous-win-over-denmark-live-reaction"
    linkGetDetail = (
        f"https://content.guardianapis.com/{id}?show-fields=bodyText&api-key={apiKey}"
    )
    response_API = requests.get(linkGetDetail)
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json["response"]["content"]
    # return jsonify({"status": "success", "trendingResults": parse_json["response"]})


def save_wordcloud(text):
    # text = "XXXssss sadasdas, asdasdasdas ssss ssss ssss, asdasdasdas "
    word_cloud = WordCloud(collocations=False, background_color="white").generate(text)
    # plt.imshow(word_cloud, interpolation='bilinear')
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    fileName = "wordcloud"
    plt.savefig(os.path.join(PATH_TO_SAVE, fileName))
    return fileName


def get_wordCount(text):
    stop_words = set(stopwords.words("english"))

    for char in "-.,\n":
        text = text.replace(char, " ")
    text = text.lower()
    word_list = text.split()
    word_list = [w for w in word_list if not w in stop_words]
    wordCount = Counter(word_list).most_common()

    result, count = [], 0
    for i in wordCount:
        count += 1
        tmp = {"word": i[0], "count": i[1]}
        result.append(tmp)
        if count > 11:
            break

    return result


if __name__ == "__main__":
    app.config["JSON_AS_ASCII"] = False
    app.run()
