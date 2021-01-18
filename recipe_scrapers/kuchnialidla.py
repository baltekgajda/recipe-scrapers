from ._abstract import AbstractScraper

from ._utils import normalize_string


class KuchniaLidla(AbstractScraper):
    @classmethod
    def host(cls):
        return "kuchnialidla.pl"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        container = self.soup.find("div", {"id": "opis"})
        if container is None:
            return None

        return "\n".join(
            normalize_string(instruction.get_text()) for instruction in container.findAll("p"))

    def ratings(self):
        return self.schema.ratings()
