from bs4 import BeautifulSoup
import requests
from recipe_scrapers import scrape_me


def get_links(page_url):
    links = []
    r = requests.get(page_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for recipe in soup.find_all("div", {"class": "recipe-index-item col-md-6 col-sm-12"}):
        for h2 in recipe.find_all("h2"):
            links.append("https://www.mojegotowanie.pl" + str(h2.find("a", href=True)["href"]))

    return links


recipes_urls = []
recipes_count = 100

i = 0
page_no = 1
while i < recipes_count:
    new_links = get_links("https://www.mojegotowanie.pl/przepisy-uzytkownikow?page=" + str(page_no))
    recipes_urls = recipes_urls + new_links
    i += len(new_links)
    page_no += 1

for url in recipes_urls:
    scraper = scrape_me(url)