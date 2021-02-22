from ._abstract import AbstractScraper
from bs4 import NavigableString
from ._utils import normalize_string, get_yields


class DomoweWypieki(AbstractScraper):
    def __init__(self,
                 url,
                 exception_handling=True,
                 meta_http_equiv=False,
                 proxies=None,
                 test=False,
                 timeout=None,
                 wild_mode=False,
                 ):
        super().__init__(url, exception_handling, meta_http_equiv, proxies, test, timeout, wild_mode)
        recipe = self.soup.find("div", {"class": "articleBody"})

        self.recipe_elements = [elem for elem in recipe]
        self.recipe_elements_str = [str(elem) for elem in recipe]

        after_description_div = "<div id=\"position-after-recipe-description\"></div>"
        after_ingredients_div = "<div id=\"position-after-recipe-ingredients\"></div>"
        after_instructions_div = "<div id=\"position-after-recipe-instructions\"></div>"
        try:
            self.ind_after_descr = self.recipe_elements_str.index(after_description_div)
            self.ind_after_ingr = self.recipe_elements_str.index(after_ingredients_div)
            self.ind_after_instr = self.recipe_elements_str.index(after_instructions_div)
        except ValueError:
            self.ind_after_descr = self.ind_after_ingr = self.ind_after_instr = 0

    @classmethod
    def host(cls):
        return "domowe-wypieki.pl"

    def author(self):
        return None

    def title(self):
        header = self.soup.find("div", {"class": "page-header"})
        if not header:
            return None

        return normalize_string(header.get_text())

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.schema.yields())

    def image(self):
        image = self.soup.find("img", {"id": "article-img-1", "data-src": True})
        if image is None:
            image = self.soup.find("img", {"class": "article-img", "data-src": True})
        return image["data-src"] if image else None

    def ingredients(self):
        ingredients = []
        for i in range(self.ind_after_descr, self.ind_after_ingr):
            container = self.recipe_elements[i]
            ingredients.extend(self.__read_ingredients_from_container(container))
        return ingredients

    def instructions(self):
        instructions = ""
        for i in range(self.ind_after_ingr, self.ind_after_instr):
            container = self.recipe_elements[i]
            instructions += self.__read_instructions_from_container(container)
        return instructions

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        container = self.soup.find("div", {"id": "recipe-description"})
        if container:
            parts = [normalize_string(part.get_text()) for part in container.findAll("p")]
        else:
            parts = []
            for i in range(self.ind_after_descr):
                container = self.recipe_elements[i]
                if container.name == "p":
                    parts.append(normalize_string(container.get_text()))
        return "\n".join(parts).strip()

    def __read_ingredients_from_container(self, container):
        print(container)
        if isinstance(container, NavigableString):
            return []
        if container.name == "p":
            return [normalize_string(container.get_text())]
        elif container.name == 'ul':
            ingredients_part = container.findAll("li")
            return [normalize_string(ingredient.get_text()) for ingredient in ingredients_part]
        elif container.get("id") is not None and container.get("id") == 'recipe-ingredients':
            ingredients = []
            for inner_container in container:
                ingredients.extend(self.__read_ingredients_from_container(inner_container))
            return ingredients
        else:
            return []

    def __read_instructions_from_container(self, container):
        if isinstance(container, NavigableString):
            return ""
        if container.get("id") is not None and container.get("id") == 'recipe-instructions':
            instructions = []
            parts = container.findAll("ol")
            for part in parts:
                instructions = instructions + [normalize_string(item.get_text()) for item in part.findAll("li")]

            return "\n".join(instructions)
        elif container.name == 'ol':
            instructions = [normalize_string(item.get_text()) for item in container.findAll("li")]
            return "\n".join(instructions)

        return ""
