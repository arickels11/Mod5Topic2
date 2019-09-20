import unittest
from input_loops import average_input_scores


class MyTestCase(unittest.TestCase):  # averages
    def test_loop(self):
        self.assertEqual(80, average_input_scores.average([60, 70, 80, 90, 100]))


if __name__ == '__main__':
    unittest.main()
