import unittest

from textstats import word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words_separated_by_whitespace(self):
        self.assertEqual(word_count("the quick  brown\nfox"), 4)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()
