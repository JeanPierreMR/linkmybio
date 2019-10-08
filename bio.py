#coding=utf-8
from flask import Flask, jsonify, render_template, request
import os,optparse, json, yaml
app = Flask(__name__)
environment = "development"

with open("links.yaml") as f:
    full_yaml = yaml.load(f, Loader=yaml.FullLoader)
    links = full_yaml["links"]
    profile = full_yaml["profile"]

@app.route("/")
def home():
    return render_template("tree.html", links = links, profile = profile)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)
