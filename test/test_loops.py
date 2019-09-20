import unittest
from input_loops import average_input_scores


class MyTestCase(unittest.TestCase):  # averages
    def test_loop(self):
        self.assertEqual(80, average_input_scores.average([60, 70, 80, 90, 100]))

    def test_loop_float(self):
        self.assertAlmostEqual(2.3333333, average_input_scores.average([2, 2, 3]))

    def test_loop_3(self):
        self.assertEquals(-20, average_input_scores.average([-10, -20, -30]))


if __name__ == '__main__':
    unittest.main()
