from tests import ScraperTest

from recipe_scrapers.noizz import Noizz


class TestNoizzScraper(ScraperTest):

    scraper_class = Noizz

    def test_host(self):
        self.assertEqual("noizz.pl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Racuchy z pieczarkami", self.harvester_class.title())

    def test_description(self):
        self.assertEqual(
            "Jeśli szukasz przepisu na danie niepozorne, ale za to pysznie zaskakujące - dobrze trafiłeś. Racuchy z pieczarkami to przesmaczne sakiewki z jesiennymi smakami. Ich przygotowanie zajmie ci mniej czasu niż szukanie kolejnego serialu na długie jesienne wieczory, a sprawi ogromną przyjemność, do której na pewno wrócisz.",
            self.harvester_class.description(),
        )

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual('None', self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "Oliwa 2 łyżki",
                "Cebula 1",
                "Pieczarki 250 g",
                "Pieprz ½ łyżeczki",
                "Sól ½ łyżeczki",
                "Pietruszka ½ pęczka",
                "Ugotowane ziemniaki 500 g",
                "Jajko 1",
                "Mąka pszenna ½ szklanki",
                "Sól ½ łyżeczki",
                "Pieczarki",
                "Ser żółty"
            ], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual("", self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(0, self.harvester_class.ratings())
