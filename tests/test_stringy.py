import unittest
from stringy import *


class TestStringy(unittest.TestCase):
    def test_concatenation(self):
        result = concat("Hello ", "world")
        self.assertEqual("Hello world", result)

    def test_get_letter_in_string(self):
        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", 12)
        self.assertEqual("m", result)

        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", 7).upper()
        self.assertEqual("H", result)

    def test_song_lyrics(self):
        result = bottles_of_beer(0)
        self.assertEqual("No bottles of beer on the wall, how sad", result)

        result = bottles_of_beer(1)
        self.assertEqual("One bottle of beer on the wall", result)

        result = bottles_of_beer(33)
        self.assertEqual("33 bottles of beer on the wall", result)

        result = bottles_of_beer("Not a number")
        self.assertEqual("This is weird", result)
