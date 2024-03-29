import unittest
from stringy import *

text_to_search = "Once upon a time, in a galaxy far, far away, " \
                        "it was a dark and stormy night when a robot " \
                        "rolled into a bar."

alphabet = "abcdefghijklmnopqrstuvwxyz"

class TestStringy(unittest.TestCase):
    def test_concatenation(self):
        result = concat(" Hello ", " world ")
        self.assertEqual("Hello world", result)

    def test_get_letter_in_string(self):
        result = get_letter_in_string(alphabet, 12)
        self.assertEqual("m", result)

        result = get_letter_in_string(alphabet, 7).upper()
        self.assertEqual("H", result)

        # Python negative indexes start at the end and go backwards
        result = get_letter_in_string(alphabet, -5)
        self.assertEqual("v", result)

    def test_get_letter_in_string_with_exceptions(self):
        # index out of bounds forwards
        result = get_letter_in_string(alphabet, 27)
        self.assertEqual("Error, index out of bounds", result)

        # index out of bounds backwards
        result = get_letter_in_string(alphabet, -27)
        self.assertEqual("Error, index out of bounds", result)

    def test_song_lyrics(self):
        # https://www.youtube.com/watch?v=xCHYR3wRQLQ
        result = bottles_of_beer(1)
        self.assertEqual("One bottle of beer on the wall", result)

        result = bottles_of_beer(5)
        self.assertEqual("5 bottles of beer on the wall", result)

        result = bottles_of_beer(66)
        self.assertEqual("66 bottles of beer on the wall", result)

    def test_song_lyrics_exceptions(self):
        result = bottles_of_beer(0)
        self.assertEqual("No bottles of beer on the wall, how sad", result)

        result = bottles_of_beer(-1)
        self.assertEqual("Go to the store and buy some more", result)

        result = bottles_of_beer("Not a number")
        self.assertEqual("This is weird", result)

        result = bottles_of_beer("!@#$%^&*()")
        self.assertEqual("This is weird", result)

    def test_is_string_in_text(self):
        result = is_string_in_text(text_to_search, "robot")
        self.assertEqual(True, result)

        result = is_string_in_text(text_to_search, "sheep")
        self.assertEqual(False, result)

    def test_where_string_in_text(self):
        result = where_in_string_is_text(text_to_search, "Once")
        self.assertEqual(0, result)

        result = where_in_string_is_text(text_to_search, "robot")
        self.assertEqual(19, result)

        # case-sensitive search
        result = where_in_string_is_text(text_to_search, "once")
        self.assertEqual("Search string not found", result)

    def test_case_insensitive_search(self):
        result = case_insensitive_search(text_to_search, "ROBOT")
        self.assertEqual(19, result)

        result = case_insensitive_search(text_to_search, "GaLaXy")
        self.assertEqual(6, result)

        result = case_insensitive_search(text_to_search, "Muppet")
        self.assertEqual("Search string not found", result)