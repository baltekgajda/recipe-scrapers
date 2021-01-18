from tests import ScraperTest

from recipe_scrapers.cookidoo import Cookidoo


class TestCookidooScraper(ScraperTest):
    scraper_class = Cookidoo

    def test_host(self):
        self.assertEqual("cookidoo.pl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Vorwerk International & Co. KmG", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Wielkanocny placek ziemniaczany", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(135, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("10 porcji", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/4c015e58-70ad-46c0-bcef-2c7ef724f8b5/Derivates/9c735783-28ea-4713-90f1-437538eafb76.jpg",
            self.harvester_class.image())

    def test_ingredients(self):
        self.maxDiff = None
        self.assertCountEqual(
            [
                "700 g wody",
                "500 g surowego boczku, bez kości, bez skóry",
                "200 - 250 g wątroby",
                "1 liść laurowy, suszony",
                "2 - 3 ziarna ziela angielskiego",
                "250 g cebuli",
                "20 g oleju rzepakowego",
                "50 g kaszy manny",
                "1500 g ziemniaków, mączystych",
                "1 łyżeczka gałki muszkatołowej, mielonej",
                "1 łyżeczka imbiru, suszonego, mielonego",
                "2 łyżki majeranku, suszonego",
                "1 - 2 łyżeczki pieprzu czarnego, mielonego",
                "2 łyżeczki soli",
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual("", self.harvester_class.instructions())

    def test_nutrients(self):
        self.assertEqual({
            'calories': '453.4 kcal',
            'carbohydrateContent': '34.6 g',
            'fatContent': '30.2 g',
            'proteinContent': '14.3 g'},
            self.harvester_class.nutrients())
