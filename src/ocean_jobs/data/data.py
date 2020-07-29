import pandas as pd
from flask import Blueprint, request, redirect, url_for

data = Blueprint("data", __name__)


@data.route("/search", methods=["POST"])
def search():
    search = dict()
    search["role"] = request.form.get("role")
    search["company"] = request.form.get("company", "")
    search["keywords"] = request.form.get("keywords", "").split(";")
    search["keywords"] = [
        keyword.strip() for keyword in search["keywords"] if keyword != ""
    ]
    search["schedule"] = request.form.get("schedule", False) == True

    # TODO:
    return redirect(url_for("views.apply"))


@data.route("/searchresults")
def searchresults():
    # TODO: Trigger TotalJobs Scraper
    df = pd.read_csv("data/raw/totaljobs.csv")
    return df.to_json(orient="records")
