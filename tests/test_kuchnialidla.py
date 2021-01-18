from tests import ScraperTest

from recipe_scrapers.kuchnialidla import KuchniaLidla


class TestKuchniaLidlaScraper(ScraperTest):
    scraper_class = KuchniaLidla

    def test_host(self):
        self.assertEqual("kuchnialidla.pl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Lidl", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Kotlety mielone z młodymi ziemniakami i mizerią", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("Liczba porcji - 4", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://kuchnialidla.pl/img/PL/960x540/df993d512ffe-6ec85e05c178-Kotlety_mielone_z_mlodymi_ziemniakami_i_mizeria_1250x700.jpg",
            self.harvester_class.image())

    def test_ingredients(self):
        self.assertCountEqual([
            "mięso mielone (np. szynka, karkówka, łopatka) – 500 g",
            'średnia cebula – 1 szt.',
            "bułka (np. kajzerka) – 1 szt.",
            "mleko lub woda do namoczenia bułki",
            "jajko – 1 szt.",
            "sól – 1 łyżeczka",
            "pieprz czarny, mielony – 1 szczypta",
            "suszone oregano – 1 szczypta",
            "suszony tymianek – 1 szczypta",
            "bułka tarta do obtoczenia kotletów",
            "smalec lub masło klarowane",
            "olej rzepakowy",
            "ugotowane, młode ziemniaki",
            "mizeria",
            "świeży koperek",
        ], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual("\n".join(
            [
                "Bułkę zalewamy mlekiem lub wodą i odstawiamy na ok. 10-15 minut.",
                "Na patelni, na rozgrzanym oleju smażymy cebulę pokrojoną w kostkę, aż się zarumieni. Odstawiamy do wystudzenia.",
                "W dużej misce łączymy mięso mielone z podsmażoną cebulą. Dodajemy bułkę dokładnie odciśniętą z mleka, jajko, sól, pieprz, oregano i tymianek. Całość wyrabiamy dłonią, aż mięso połączy się z pozostałymi składnikami w jednolitą masę. Jeśli masa okaże się zbyt sucha, dodajemy odrobinę wody i ponownie wyrabiamy. Jeśli uzyskamy zbyt rzadką masę, dodajemy 1 łyżkę bułki tartej i ponownie wyrabiamy całość, aż do uzyskania pożądanej konsystencji.",
                "Z dokładnie wyrobionego mięsa formujemy owalne, lekko spłaszczone kotlety i obtaczamy je w bułce tartej. Mielone smażymy na patelni, na rozgrzanym smalcu (lub maśle klarowanym) ok. 3-4 minut z każdej strony – początkowo na dużym ogniu, który po kilku chwilach zmniejszamy.Podajemy z ugotowanymi, młodymi ziemniakami i mizerią. Z wierzchu posypujemy świeżym, drobno posiekanym koperkiem.",
            ]),
            self.harvester_class.instructions()
        )