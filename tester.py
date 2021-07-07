from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://noizz.pl/jedzenie/pieczone-golabki-faszerowane-kasza-warzywami-i-pieczarkami-z-sosem-maslankowo/xcm77ym')

print(scraper.title())
print(scraper.author())
print(scraper.total_time())
print(scraper.yields())
print(scraper.ingredients())
print(scraper.instructions())
print(scraper.description())
print(scraper.image())
