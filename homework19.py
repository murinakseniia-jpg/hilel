import requests
import csv
from bs4 import BeautifulSoup

Headers = { "User-Agent": "homework-hillel/1.0 (practice)" }
b_url = "https://quotes.toscrape.com/tag/life/"

def p_page(url):
    response = requests.get( url, headers=Headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup( response.text, "lxml")

    rows = [
        {
            "author":quote.select_one("small.author").get_text(strip=True),
            "text": quote.select_one("span.text").get_text(strip=True)
        }
        for quote in soup.select( "div.quote" )
    ]

    return rows

def life(data):
    with open("life.csv", "w", newline="", encoding="utf-8" ) as file:
        writer = csv.DictWriter(file, fieldnames=["author", "text"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__" :
    data = p_page(b_url)
    life(data)