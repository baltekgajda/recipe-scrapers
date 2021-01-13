from recipe_scrapers import scrape_me


# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://smaker.pl/przepisy-desery/przepis-ciasto-quot-sloneczko-quot-bez-blaszki,185837,koral.html')

print(scraper.title())
print(scraper.total_time())
print(scraper.yields())
print(scraper.ingredients())
print(scraper.instructions())
print(scraper.image())
print(scraper.host())
print(scraper.links())
print(scraper.nutrients())