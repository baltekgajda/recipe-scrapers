from tests import ScraperTest

from recipe_scrapers.kwestiasmaku import KwestiaSmaku


class TestKwestiaSmakuScraper(ScraperTest):
    scraper_class = KwestiaSmaku

    def test_host(self):
        self.assertEqual('przepisy.pl', self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.chefkoch.de/rezepte/1170311223132029/Hackbraten-supersaftig.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            'Placki ziemniaczane',
            self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(
            40,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            '8 serving(s)',
            self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                'ziemniaki 1 kilogram',
                'cebula 1 sztuka',
                'jajka 2 sztuki',
                'Przyprawa w Mini kostkach Czosnek Knorr 1 sztuka',
                'Gałka muszkatołowa z Indonezji Knorr 1 szczypta',
                'sól 1 szczypta',
                'mąka 3 łyżki'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            'Obierz ziemniaki, zetrzyj na tarce. Odsącz masę przez sito. Zetrzyj cebulę na tarce.\nDodaj do ziemniaków cebulę, jajka, gałkę muszkatołową oraz mini kostkę Knorr.\nWymieszaj wszystko dobrze, dodaj mąkę, aby nadać masie odpowiednią konsystencję.\nRozgrzej na patelni olej, nakładaj masę łyżką. Smaż placki z obu stron na złoty brąz i od razu podawaj.',
            self.harvester_class.instructions()
        )
