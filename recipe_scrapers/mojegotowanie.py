from ._abstract import AbstractScraper

from ._utils import normalize_string


class MojeGotowanie(AbstractScraper):
    @classmethod
    def host(cls):
        return "mojegotowanie.pl"

    def author(self):
        container = self.soup.find("div", {"class": "recipe-author"})
        if container is None:
            return ""

        return container.find("a").get_text()

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
        container = self.soup.find("div", {"class": "recpie-ingredient"})
        if container is None:
            return []

        return [normalize_string(ingredient.get_text()) for ingredient in container.findAll("li")]

    def instructions(self):
        container = self.soup.find("div", {"class": "row preparationSteps"})
        if container is None:
            return []

        instructions = []
        for instruction in container.findAll('span'):
            if not instruction.has_attr('class'):
                instructions.append(normalize_string(instruction.get_text()))

        if len(instructions) > 0:
            return "\n".join(instructions)

        for instruction in container.findAll(['span', 'li'], {"itemprop": "name"}):
            instructions.append(normalize_string(instruction.get_text()))
        return "\n".join(instructions)

    def description(self):
        description = self.soup.find("meta", {"property": "og:description", "content": True})
        return description.get("content")
