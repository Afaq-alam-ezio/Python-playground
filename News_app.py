import requests
import json


query = input("Enter the news related keyword = ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-02-03&sortBy=publishedAt&apiKey=0ddc2536ce834edfba6bbf3a2ae1b92e"
req = requests.get(url)
news = json.loads(req.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
