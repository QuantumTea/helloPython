import unittest
import csv


class TestCsv(unittest.TestCase):
    def test_file_can_be_read(self):
        result = csv.does_file_exist()
        # print(result)
        self.assertIn("Day,Word count,Daily total", result)
