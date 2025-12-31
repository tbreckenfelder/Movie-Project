import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
Base_url = f"http://www.omdbapi.com/"


def movie_fetcher(title):
    params = {"t": title, "apikey": API_KEY}
    response = requests.get(Base_url, params=params)
    data = response.json()

    if data["Response"] == "False":
        print("Movie '" + title + "' not found.")
        return {}
    return {"title": data["Title"], "year": data["Year"], "rating": data["imdbRating"], "poster": data["Poster"] }


