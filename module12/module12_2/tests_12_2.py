import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        for index, result in enumerate(cls.all_results, start=1):
            print(f"Соревнование №{index}:")
            for place, runner in result.items():
                print(f"{place:4} место - {runner}")
            print()

    def setUp(self):
        super().setUp()
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrey = Runner(name="Андрей", speed=9)
        self.nik = Runner(name="Ник", speed=3)

    def test1(self):
        tournament = Tournament(90, self.usain, self.nik)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1] == {1: "Усэйн", 2: "Ник"})

    def test2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1] == {1: "Андрей", 2: "Ник"})

    def test3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1] == {1: "Усэйн", 2: "Андрей", 3: "Ник"})
