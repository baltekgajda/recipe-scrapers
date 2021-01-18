from ._abstract import AbstractScraper

from ._utils import normalize_string


class MojeWypieki(AbstractScraper):
    @classmethod
    def host(cls):
        return "mojewypieki.com"

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
        container = self.soup.find("div", {"class": "article__content"})
        if container is None:
            return []

        ingredients = []
        for item in container:
            if item.name == "h2":
                text = item.find("u")
                if text is None:
                    continue
                else:
                    ingredients.append(text.get_text())
            elif item.name == 'ul':
                ingredients_part = item.findAll("li")
                ingredients = ingredients + [ingredient.get_text() for ingredient in ingredients_part]
            else:
                continue
        return [normalize_string(ingredient) for ingredient in ingredients]

    def instructions(self):
        container = self.soup.find("div", {"class": "article__content"})
        if container is None:
            return []

        instructions = []
        for item in container:
            if item.name == "p":
                instructions.append(item)
        return "\n".join([normalize_string(instruction.get_text()) for instruction in instructions])

    def ratings(self):
        return self.schema.ratings()
