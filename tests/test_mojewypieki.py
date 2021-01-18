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
        self.maxDiff = None
        self.assertCountEqual(
            [
                "Składniki na spód brownie:",
                "60 g masła",
                "100 g deserowej lub gorzkiej czekolady",
                "1 duże jajko",
                "1 łyżeczka ekstraktu z wanilii",
                "70 g drobnego cukru do wypieków",
                "30 g mąki pszennej",
                "Składniki na masę serową:",
                "1 kg twarogu półtłustego lub tłustego zmielonego trzykrotnie*",
                "8 dużych jajek",
                "100 g masła",
                "220 g drobnego cukru do wypieków",
                "3 łyżki cukru wanilinowego",
                "3 łyżki skrobi ziemniaczanej",
                "1 szklanka kandyzowanej skórki pomarańczowej",
                "Składniki na lukier:",
                "1 szklanka cukru pudru",
                "3 – 4 łyżki gorącej wody",
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        self.maxDiff = None
        self.assertEqual(
            "\n".join([
                "Wszystkie składniki powinny być w temperaturze pokojowej.",
                "W garnuszku roztopić masło, zdjąć z palnika. Do gorącego dodać posiekaną gorzką czekoladę, odstawić na 2 minuty. Po tym czasie wymieszać do powstania gładkiego sosu czekoladowego.",
                "W naczyniu lekko roztrzepać jajko rózgą kuchenną (nie ubijać). Dodać ekstrakt z wanilii, cukier, wymieszać rózgą kuchenną. Dodać jeszcze ciepły sos czekoladowy, wymieszać rózgą kuchenną. Wsypać przesianą mąkę, wymieszać tylko do połączenia się składników.",
                "Mieszankę czekoladową przelać do formy o wymiarach 31 x 22 cm wyłożonej wcześniej papierem do pieczenia. Wyrównać. Piec około 13 minut w temperaturze 160ºC lub do wypieczenia (patyczek włożony w w ciasto może być oblepiony od czekolady, ale nie może być na nim śladów surowego ciasta).",
                "Wszystkie składniki powinny być w temperaturze pokojowej.",
                "Masło i oba cukry utrzeć w misie miksera do otrzymania jasnej, puszystej masy maślanej. Ucierając, dodawać po 1 żółtku i części twarogu. Ucierać, aż składniki się połączą i masa będzie puszysta. Wmiksować skrobię ziemniaczaną i kandyzowaną skórkę pomarańczową.",
                "Białka ubić na sztywno. Pianę wmieszać delikatnie do masy serowej.",
                "Upieczony spód brownie wyjąć z piekarnika. Wyłożyć na niego masę serową, wyrównać.",
                "Sernik świąteczny piec około 70 minut w temperaturze 170°C, najlepiej bez termoobiegu. Wystudzić w lekko uchylonym piekarniku, następnie wystudzić przez noc. Przed podaniem polukrować.",
                "Nie ma konieczności przechowywania sernika w lodówce.",
                "Cukier puder wsypać do miseczki. Rozetrzeć z gorącą wodą przy pomocy wypukłej strony łyżki. Gdy lukier będzie zbyt gęsty – dodać odrobinę wody. Gdy będzie zbyt rzadki, dosypać cukru pudru.",
                "* Przy użyciu bardzo tłustego sera z wiaderka (zawartość tłuszczu ponad 18%) ilość masła można zmniejszyć o połowę lub nawet o 3/4. Wtedy masła w masie serowej będzie mało i nie utrze się z cukrem na puch, dlatego razem z masłem i cukrem ucieramy również żółtka a następnie dodajemy pozostałe składniki.",
                "Smacznego :-).",
                "",
            ]),
            self.harvester_class.instructions()
        )
