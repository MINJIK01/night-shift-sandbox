import unittest

from textstats import char_frequency, word_count


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


class CharFrequencyTest(unittest.TestCase):
    def test_counts_each_character(self):
        self.assertEqual(char_frequency("aab"), {"a": 2, "b": 1})

    def test_whitespace_is_not_counted(self):
        result = char_frequency("a b\tc\nd")
        for ws in (" ", "\t", "\n"):
            self.assertNotIn(ws, result)
        self.assertEqual(result, {"a": 1, "b": 1, "c": 1, "d": 1})

    def test_case_sensitive(self):
        self.assertEqual(char_frequency("Aa"), {"A": 1, "a": 1})

    def test_empty_and_blank_text(self):
        self.assertEqual(char_frequency(""), {})
        self.assertEqual(char_frequency("   "), {})

    def test_punctuation_is_counted(self):
        self.assertEqual(char_frequency("a!!"), {"a": 1, "!": 2})

    def test_returns_dict(self):
        self.assertIsInstance(char_frequency("abc"), dict)


if __name__ == "__main__":
    unittest.main()
