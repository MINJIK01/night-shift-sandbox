import unittest

from textstats import word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words_separated_by_whitespace(self):
        self.assertEqual(word_count("the quick  brown\nfox"), 4)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)

    def test_punctuation_only_token_is_not_a_word(self):
        self.assertEqual(word_count("hello , world"), 2)

    def test_punctuation_attached_to_word_counts_as_one_word(self):
        self.assertEqual(word_count("hello world!"), 2)

    def test_only_punctuation_tokens_have_no_words(self):
        self.assertEqual(word_count(", . ! -"), 0)


if __name__ == "__main__":
    unittest.main()
