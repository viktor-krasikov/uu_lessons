import unittest
from unittest import skipIf

from runner_and_tournament import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        walker = Runner("walker")
        for _ in range(10):
            walker.walk()
        self.assertEqual(50, walker.distance)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(100, runner.distance)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        walker = Runner("walker")
        runner = Runner("runner")
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
