from ._abstract import AbstractScraper

from ._utils import normalize_string


class MojeGotowanie(AbstractScraper):
    @classmethod
    def host(cls):
        return "mojegotowanie.pl"

    def author(self):
        return self.schema.author()

    def title(self):
        title = self.soup.find("meta", {"property": "og:title", "content": True})
        return title.get("content")

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        container = self.soup.find("ul", {"class": "recpie-ingredient-list"})
        if container is None:
            return []

        return [normalize_string(ingredient.get_text()) for ingredient in container.findAll("li")]

    def instructions(self):
        container = self.soup.find("ul", {"itemprop": "step"})
        if container is None:
            return ""

        instructions = []
        for instruction in container.findAll(['span', 'li'], {"itemprop": "name"}):
            instructions.append(normalize_string(instruction.get_text()))
        return "\n".join(instructions)

    def description(self):
        description = self.soup.find("div", {"itemprop": "description"})
        if not description:
            return None

        return description.get_text() if description else None
