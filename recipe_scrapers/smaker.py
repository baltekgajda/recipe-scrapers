from ._abstract import AbstractScraper

from ._utils import get_minutes, normalize_string, get_yields


class Smaker(AbstractScraper):
    @classmethod
    def host(cls):
        return "smaker.pl"

    def author(self): #TODO
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.schema.yields())

    def image(self):
        image = self.soup.find("div", {"class": "image_wrap"}).find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self): #TODO
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        d = normalize_string(self.soup.find("div", {"class": "userDescriptionHint"}).get_text())
        return d if d else None
