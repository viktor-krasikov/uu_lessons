import unittest

from runner_and_tournament import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = Runner("walker")
        for _ in range(10):
            walker.walk()
        self.assertEqual(50, walker.distance)

    def test_run(self):
        runner = Runner("runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(100, runner.distance)

    def test_challenge(self):
        walker = Runner("walker")
        runner = Runner("runner")
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
