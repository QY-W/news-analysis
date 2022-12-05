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
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import gensim
import gensim.corpora as corpora
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
import spacy
import pickle
import re
import pyLDAvis
import pyLDAvis.gensim_models
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn.decomposition import LatentDirichletAllocation


import pymongo
from cryptography.fernet import Fernet
import re


# configuration
DEBUG = True

# instantiate the app

app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

# Init
APIKEY = "58de53b7-a9ef-45d9-bf11-60072288147d"
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PATH_TO_SAVE = os.path.join(BASE_DIR, "frontend/src/assets")
PATH_TO_PUBLIC = os.path.join(BASE_DIR, "frontend/public")


# MongoDB set up
url = "mongodb+srv://330-creative:jQeQD3ktzqzhZJB6@cluster0.ciqs10o.mongodb.net/?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(url)
# myclient.test.authenticate( DATABASE_USERNAME , DATABASE_PASSWORD )
mydb = myclient["cse330"]
key = Fernet.generate_key()
username_regex = re.compile(r"^[\w_\-]+$")


# sanity check route
@app.route("/open", methods=["GET"])
def open_door():
    return jsonify("Connected TO FLASK ! >_<")


@app.route("/trending", methods=["GET"])
def show_list():
    # apiKey = "58de53b7-a9ef-45d9-bf11-60072288147d"
    # searchContent = "trump"
    link2 = "https://content.guardianapis.com/search?&api-key=test"  # "https://content.guardianapis.com/search?q=&api-key=test"
    # link = f"https://content.guardianapis.com/search?q={searchContent}&api-key={apiKey}"
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
        # score
        senti_score = get_sentiment_scores(content)
        # LDA
        get_LDA(content)
        return jsonify(
            {
                "status": "success",
                "detailResults": result,
                "wordcloud": cloudFileName,
                "wordcount": wordCount,
                "score": senti_score,
            }
        )


# Detail text analysis helper functions


def get_detail(id):
    linkGetDetail = (
        f"https://content.guardianapis.com/{id}?show-fields=bodyText&api-key={APIKEY}"
    )
    response_API = requests.get(linkGetDetail)
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json["response"]["content"]


def save_wordcloud(text):

    word_cloud = WordCloud(collocations=False, background_color="white").generate(text)
    # plt.imshow(word_cloud, interpolation='bilinear')
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    fileName = "wordcloud"
    plt.savefig(os.path.join(PATH_TO_SAVE, fileName))
    return fileName


def get_wordCount(text):
    stop_words = set(stopwords.words("english"))

    for char in '"“”:–-.,\n':
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


def get_sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return sentiment_dict["compound"]


def get_LDA(raw):
    for char in "–-.,\n":
        raw = raw.replace(char, " ")
    stop_words = set(stopwords.words("english"))
    # for w in stop_words:
    #     raw = raw.replace(w, " ")

    text = raw.lower()
    toy_corpus = [text.split(".") for t in text][0]
    tweets = [t.split(" ") for t in toy_corpus]
    id2word = Dictionary(tweets)
    corpus = [id2word.doc2bow(text) for text in tweets]
    lda_model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        num_topics=10,
        random_state=0,
        chunksize=100,
        alpha="auto",
        per_word_topics=True,
    )
    p = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
    pyLDAvis.save_html(p, "../frontend/lda.html")


@app.route("/search", methods=["GET", "POST"])
def show_search():
    if request.method == "POST":
        context = request.get_json(force=True)
        searchContent = context["searchText"]
        sortMethod = context["sortMethod"]
        link = f"https://content.guardianapis.com/search?q={searchContent}&order-by={sortMethod}&api-key={APIKEY}"

        boolUseFilter = context["filter"]
        if boolUseFilter:
            dFrom = context["from"]
            dTo = context["to"]
            link = f"https://content.guardianapis.com/search?q={searchContent}&from-date={dFrom}&to-date={dTo}&order-by={sortMethod}&api-key={APIKEY}"
        response_API = requests.get(link)
        # response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
        print(response_API.status_code)
        data = response_API.text
        parse_json = json.loads(data)
        results = parse_json["response"]["results"]
        return jsonify({"status": "success", "searchResults": results})


@app.route("/login", methods=["GET", "POST"])
def user_ret():
    if request.method == "POST":
        context = request.get_json(force=True)
        method = context["method"]
        username = context["username"]
        password = context["password"]
        if method == "login":
            state = log_in(username, password)
            return jsonify(
                {
                    "status": state,
                    "loginResults": "login",
                    "ori": context,
                }
            )
        elif method == "register":
            state = insert_user(username, password)
            return jsonify(
                {
                    "status": state,
                    "loginResults": "register",
                    "ori": context,
                }
            )


# MONGO DB helper functions
def check_username(username):
    match = username_regex.match(username)
    if match is None:
        print("Invalid username.")
        return 0
    else:
        n = 0
        find = mydb["users"].find({"username": username})
        for x in find:
            if x is not None:
                n = n + 1
        if n > 0:
            print("This username has been used.")
            return 0
        else:
            return 1


def insert_user(username, password):
    # username check
    if check_username(username) == 0:
        # exit()
        return 0
    else:
        # using cryptography to encode the password
        pdCrypt = encrypt(str(password).encode(), key)
        mydict = {"username": username, "password": pdCrypt, "key": key}
        x = mydb["users"].insert_one(mydict)
        # print("insert successes! id is {}".format(x.inserted_id))
        return 1


def verify_password(username, password):
    result = []
    find = mydb["users"].find({"username": username}, {"_id": 0, "username": 0})
    for x in find:
        result.append([x["password"], x["key"]])
    if len(result) != 1:
        return 0
    else:
        pw = decrypt(result[0][0], result[0][1]).decode()
        if pw == str(password):
            return 1
        else:
            return 0


def log_in(username, password):
    if verify_password(username, password):
        # print("login success")
        return 1
    else:
        # print("login fail")
        return 0


def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)


def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


if __name__ == "__main__":
    app.config["JSON_AS_ASCII"] = False
    app.run()
