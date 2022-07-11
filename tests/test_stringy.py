import unittest
from stringy import *
# https://www.youtube.com/watch?v=xCHYR3wRQLQ


class TestStringy(unittest.TestCase):
    def test_concatenation(self):
        result = concat("Hello ", "world")
        self.assertEqual("Hello world", result)

    def test_get_letter_in_string(self):
        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", 12)
        self.assertEqual("m", result)

        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", 7).upper()
        self.assertEqual("H", result)

        # Python negative indexes start at the end and go backwards
        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", -5)
        self.assertEqual("v", result)

    def test_get_letter_in_string_with_exceptions(self):
        # index out of bounds
        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", 27)
        self.assertEqual("Exception, index out of bounds", result)

        # Python negative indexes start at the end and go backwards
        result = get_letter_in_string("abcdefghijklmnopqrstuvwxyz", -27)
        self.assertEqual("Exception, index out of bounds", result)

    def test_song_lyrics(self):
        result = bottles_of_beer(0)
        self.assertEqual("No bottles of beer on the wall, how sad", result)

        result = bottles_of_beer(1)
        self.assertEqual("One bottle of beer on the wall", result)

        result = bottles_of_beer(33)
        self.assertEqual("33 bottles of beer on the wall", result)

        result = bottles_of_beer(66)
        self.assertEqual("66 bottles of beer on the wall", result)

        result = bottles_of_beer(-1)
        self.assertEqual("Go to the store and buy some more", result)

        result = bottles_of_beer("Not a number")
        self.assertEqual("This is weird", result)
