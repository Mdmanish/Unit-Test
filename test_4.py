import unittest
import part_8
import csv


class testClass(unittest.TestCase):
    def test_calculate(self):
        file1 = open('mock_matches.csv', 'r')
        matches_data = csv.DictReader(file1)
        file2 = open('mock_deliveries.csv', 'r')
        deleveries_data = csv.DictReader(file2)
        self.assertEqual(part_8.calculate(deleveries_data, matches_data), ([
                         'AB Dinda', 'Harbhajan Singh', 'AR Patel'], [0, 0, 1]))
        file1.close()
        file2.close()


if __name__ == "__main__":
    unittest.main()
