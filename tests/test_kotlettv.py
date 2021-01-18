from tests import ScraperTest

from recipe_scrapers.kotlettv import KotletTv


class TestKotletTvScraper(ScraperTest):
    scraper_class = KotletTv

    def test_host(self):
        self.assertEqual("kotlet.tv", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Paulina Stępień", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Zupa ogórkowa", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("dla 4–6 osób", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "http://kotlet.tv/wp-content/uploads/2010/08/zupa-ogorkowa-370x370.jpg",
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "pęczek włoszczyzny",
                "1–2 słoiki <a title=\"Ogórki na zupę\" href=\"http://kotlet.tv/ogorki-na-zupe\">ogórków na zupę</a>",
                "ok. 1 łyżeczki grubo mielonego pieprzu",
                "1/2 łyżeczki soli",
                "4 łyżki śmietany 18% lub jogurtu naturalnego",
                "ok. 1,7 l wody",
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.assertEqual(
            "\n".join([
                "1. Warzywa kroję w plasterki, kostkę itp.",
                "2. Wrzucam do garnka, zalewam wodą, doprawiam przyprawami i gotuję do miękkości. Najlepiej widać po marchewce – jak miękka, to już. ;-)",
                "3. Wtedy dodaję ogórki ze słoika, mieszam, chwilkę gotuję, ale naprawdę kilka minut, by smaki się połączyły. Dodaję śmietanę lub jogurt, mieszam. Podaję z ziemniakami i makaronem, smacznego. ;-)",
            ]),
            self.harvester_class.instructions()
        )
