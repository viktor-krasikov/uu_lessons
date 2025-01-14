from unittest import TestLoader, TestSuite, TextTestRunner

import tests_12_1
import tests_12_2

my_suite = TestSuite()

my_suite.addTest(TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
my_suite.addTest(TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

my_runner = TextTestRunner(verbosity=2)
my_runner.run(my_suite)
