import unittest
import part_6
import csv


class testClass(unittest.TestCase):
    def test_calculate(self):
        output = {'Kolkata Knight Riders': {2008: 0, 2009: 0, 2010: 1, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 1, 2017: 0}, 'Royal Challengers Bangalore': {2008: 0, 2009: 0, 2010: 1, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 1}, 'Mumbai Indians': {2008: 0, 2009: 0, 2010: 1, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 1, 2016: 0,
                                                                                                                                                                                                                                                                                     2017: 0}, 'Kings XI Punjab': {2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 1, 2016: 0, 2017: 0}, 'Delhi Daredevils': {2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 1, 2016: 0, 2017: 0}, 'Rising Pune Supergiants': {2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 1, 2017: 0}}
        file = open('mock_matches.csv', 'r')
        data = csv.DictReader(file)
        self.assertEqual(part_6.calculate(data), (output))
        file.close()


if __name__ == "__main__":
    unittest.main()
