from ._abstract import AbstractScraper


class Cookidoo(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookidoo.pl"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        image = self.soup.find("img", {"class": "core-tile__image", "src": True})
        return image["src"] if image else None

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def nutrients(self):
        return self.schema.nutrients()
