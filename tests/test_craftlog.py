from tests import ScraperTest

from recipe_scrapers.craftlog import Craftlog


class TestCraftlogScraper(ScraperTest):
    scraper_class = Craftlog

    def test_host(self):
        self.assertEqual("craftlog.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("@motylek.gotuje", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Słone Ciasteczka Z Ciasta Francuskiego", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(47, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual('None', self.harvester_class.yields())

    def test_image(self):
        self.assertEqual("https://craftlog.com/m/i/11216047=s1280=h960", self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual([
            "1 płat ciasta francuskiego",
            "marchew z pieczenia żeberek",
            "mięso z żeberka lub szynka",
            "cebula",
            "6 pieczarek",
            "sól, pieprz",
            "natka pietruszki",
            "olej",
            "jajko",
            "4 plastry sera żółtego",
        ], self.harvester_class.ingredients())

    def test_instructions(self):
        self.maxDiff = None
        self.assertEqual("\n".join(
            [
                "Kroimy i smażymy pieczarki.. Pieczarki i cebulę kroimy w kostkę- smażymy, mieszamy z mięsem z upieczonych żeberek i marchew. Płat ciasta kroimy na 8 kawałków. Jedną stronę nacinamy. Smarujemy roztrzepanym jajkiem. Na każdy kawałek kładziemy 1/2 plastra sera.",
                "Super smaczne.. Na wierzch kładziemy zmieszane pozostałe składniki. Sklejamy i przyciskamy widelcem brzegi. Smarujemy roztrzepanym jajkiem. Na wierzchu można posypać serem żółtym. Pieczemy do zrumienienia w 220 stopniach.",
            ]
        ), self.harvester_class.instructions())