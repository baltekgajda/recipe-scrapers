from tests import ScraperTest

from recipe_scrapers.mojewypieki import MojeWypieki


class TestMojeWypiekiScraper(ScraperTest):
    scraper_class = MojeWypieki

    def test_host(self):
        self.assertEqual("mojewypieki.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Dorota Świątkowska", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Sernik świąteczny", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("None", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://static.mojewypieki.com/wp-content/uploads/2020/12/Sernik_swiateczny_3.jpg",
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(["todo"], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual("todo", self.harvester_class.instructions())
