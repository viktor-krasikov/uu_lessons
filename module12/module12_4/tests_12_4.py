import logging
import unittest
from unittest import skipIf

from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            walker = Runner("walker", speed=-5)
            for _ in range(10):
                walker.walk()
            self.assertEqual(50, walker.distance)
            logging.info('"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning("Неверная скорость для Runner", exc_info=e)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(-5)
            for _ in range(10):
                runner.run()
            self.assertEqual(100, runner.distance)
            logging.info('"test_run" выполнен успешно')
        except Exception as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=e)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        walker = Runner("walker")
        runner = Runner("runner")
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
