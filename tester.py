from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.mojegotowanie.pl/przepis/mule-w-sosie-serowo-pomidorowym')

print(scraper.title())
print(scraper.author())
print(scraper.total_time())
print(scraper.yields())
print(scraper.ingredients())
print(scraper.instructions())
print(scraper.image())
