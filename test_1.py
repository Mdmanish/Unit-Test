import unittest
import part_5
import csv


class testClass(unittest.TestCase):
    def test_calculate(self):
        file = open('mock_matches.csv', 'r')
        data = csv.DictReader(file)
        self.assertEqual(part_5.calculate(
            data), ({'2010': 3, '2015': 3, '2016': 2, '2017': 1}))
        file.close()

    def test_transfer(self):
        file = open('mock_matches.csv', 'r')
        data = csv.DictReader(file)
        dictionary = part_5.calculate(data)
        self.assertEqual(part_5.transfer(dictionary),
                         (['2010', '2015', '2016', '2017'], [3, 3, 2, 1]))
        file.close()


if __name__ == "__main__":
    unittest.main()
