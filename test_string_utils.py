import unittest

from string_utils import reverse_string, count_vowels
from sample_strings import SAMPLE_STRINGS


class TestReverseString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_spaces_and_case(self):
        self.assertEqual(reverse_string("Hi There"), "erehT iH")


class TestCountVowels(unittest.TestCase):
    def test_example(self):
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_empty(self):
        self.assertEqual(count_vowels(""), 0)

    def test_uppercase(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_mixed_case(self):
        self.assertEqual(count_vowels("PyThOn"), 1)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)


class TestSampleStrings(unittest.TestCase):
    """Check every sample string against an independent calculation."""

    def test_sample_count(self):
        self.assertTrue(50 <= len(SAMPLE_STRINGS) <= 70)

    def test_reverse_all_samples(self):
        for text in SAMPLE_STRINGS:
            with self.subTest(text=text):
                self.assertEqual(reverse_string(text), text[::-1])

    def test_vowels_all_samples(self):
        for text in SAMPLE_STRINGS:
            with self.subTest(text=text):
                expected = sum(1 for c in text if c in "aeiouAEIOU")
                self.assertEqual(count_vowels(text), expected)

    def test_double_reverse_returns_original(self):
        for text in SAMPLE_STRINGS:
            with self.subTest(text=text):
                self.assertEqual(reverse_string(reverse_string(text)), text)


if __name__ == "__main__":
    unittest.main()
