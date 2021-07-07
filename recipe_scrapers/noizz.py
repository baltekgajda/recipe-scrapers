from ._abstract import AbstractScraper
from ._utils import normalize_string


class Noizz(AbstractScraper):
    @classmethod
    def host(cls):
        return "noizz.pl"

    def author(self):
        return ""

    def title(self):
        return self.soup.find("div", {"class": "mainVideo"}).find("h1").text

    def description(self):
        d = normalize_string(
            self.soup.find("div", {"class": "mainVideo"}).find("div", {"class": "lead"}).text
        )
        return d if d else None

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return None

    def ingredients(self):
        ingredients = self.soup.find("div", {"class": "whitelistPremium"}).findAll("li")
        if len(ingredients) == 0:
            ingredients = self.soup.find("div", {"class": "whitelistPremium"}).findAll("p")
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        return ""

    def ratings(self):
        return 0

