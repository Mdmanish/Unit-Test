import unittest
import part_7
import csv


class testClass(unittest.TestCase):
    def test_calculate(self):
        output = {'Rising Pune Supergiants': 7, 'Kolkata Knight Riders': 6}
        file1 = open('mock_matches.csv', 'r')
        matches_data = csv.DictReader(file1)
        file2 = open('mock_deliveries.csv', 'r')
        deleveries_data = csv.DictReader(file2)
        self.assertEqual(part_7.calculate(
            deleveries_data, matches_data), (output))
        file1.close()
        file2.close()

    def test_tansfer(self):
        file1 = open('mock_matches.csv', 'r')
        matches_data = csv.DictReader(file1)
        file2 = open('mock_deliveries.csv', 'r')
        deleveries_data = csv.DictReader(file2)
        dictionary = part_7.calculate(deleveries_data, matches_data)
        self.assertEqual(part_7.transfer(
            dictionary), (['Rising Pune Supergiants', 'Kolkata Knight Riders'], [7, 6]))
        file1.close()
        file2.close()


if __name__ == "__main__":
    unittest.main()
