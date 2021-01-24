from tests import ScraperTest

from recipe_scrapers.mojegotowanie import MojeGotowanie


class TestMojeGotowanieScraper(ScraperTest):
    scraper_class = MojeGotowanie

    def test_host(self):
        self.assertEqual("mojegotowanie.pl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("/uzytkownik/gastrosfera1", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Mule w sosie serowo pomidorowym", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("None", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.mojegotowanie.pl/media/cache/default_view/uploads/media/recipe/0001/81/f7050ccb15de5360c5d63270ed9a11da463d14ee.jpeg",
            self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual([
            "ok. 1kg muli (mogą być mrożone)",
            "200 ml białego wytrawnego wina",
            "200 g serka topionego kremowego",
            "3 ząbki czosnku",
            "3 łyżki oliwy",
            "3 szalotki",
            "3 dojrzałe pomidory",
            "świeża bazylia",
            "pieprz, sól do smaku",
        ], self.harvester_class.ingredients())

    def test_instructions(self):
        self.maxDiff = None
        self.assertEqual(
            "\n".join([
                "Mule dokładnie oczyścić i umyć w zimnej wodzie. Pomidory sparzyć, obrać i pokroić w drobną kostkę. W garnku rozgrzać oliwę i wrzucić posiekany czosnek oraz szalotkę. Chwilę podsmażyć do lekkiego zrumienienia.",
                "Dodać pomidory, podlać winem, doprawić solą i pieprzem. Dodać mule, przykryć pokrywką i dusić na małym ogniu ok. 2 – 3 minuty. Mule wyciągnąć, dodać serek topiony i wszystko dokładnie zmiksować. Gotowy sos wylać na talerz, ułożyć mule i udekorować świeżą bazylią. Podawać z ulubionym pieczywem. Smacznego!",
            ]),
            self.harvester_class.instructions()
        )

    def test_description(self):
        self.assertEqual(
            "Z okazji zbliżających się Walentynek proponujemy spróbować swoich sił przygotowując dla drugiej połówki wykwintne i romantyczne danie – małże w sosie pomidorowym z dodatkiem serka topionego!",
            self.harvester_class.description(),
        )
