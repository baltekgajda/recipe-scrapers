from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.mojewypieki.com/przepis/paczki-z-ajerkoniakiem')

print(scraper.title())
print(scraper.total_time())
print(scraper.yields())
print(scraper.ingredients())
print(scraper.instructions())
print(scraper.image())
print(scraper.host())
