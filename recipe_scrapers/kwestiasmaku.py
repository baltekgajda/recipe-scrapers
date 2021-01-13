from ._abstract import AbstractScraper
from ._utils import normalize_string


class KwestiaSmaku(AbstractScraper):
    @classmethod
    def host(cls):
        return "kwestiasmaku.com"

    def title(self):
        return self.soup.schema.title()

    def ingredients(self):
        ingredients = self.soup.findAll("div", {
            "class": "field field-name-field-przygotowanie field-type-text-long field-label-above"})

        return [
            normalize_string(i.get_text()) + " " + normalize_string(j.get_text())
            for i, j in zip(ingredients[0::2], ingredients[1::2])
        ]

    def instructions(self):
        instructions = self.soup.findAll("p", {"class": "step-info-description"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
