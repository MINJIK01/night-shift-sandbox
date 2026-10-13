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

    def test_unicode_punctuation_only_tokens_have_no_words(self):
        self.assertEqual(word_count("… — 。 · “"), 0)

    def test_unicode_punctuation_attached_to_word(self):
        self.assertEqual(word_count("안녕하세요。 세계…"), 2)

    def test_em_dash_token_between_words(self):
        self.assertEqual(word_count("hello — world"), 2)

    def test_ascii_punctuation_only_still_has_no_words(self):
        self.assertEqual(word_count("!!! ..."), 0)

    def test_currency_symbol_token_counts_as_word(self):
        self.assertEqual(word_count("가격 € 5"), 3)

    def test_arrow_symbol_token_counts_as_word(self):
        self.assertEqual(word_count("→"), 1)

    def test_ascii_symbol_tokens_are_not_counted(self):
        self.assertEqual(word_count("a + b = c"), 3)

    def test_whitespace_only_text_has_no_words(self):
        self.assertEqual(word_count("   "), 0)
        self.assertEqual(word_count(" \t\r\n "), 0)

    def test_ideographic_space_separates_words(self):
        self.assertEqual(word_count("a b\u3000c"), 3)

    def test_non_breaking_space_separates_words(self):
        self.assertEqual(word_count("a\u00a0b"), 2)

    def test_mixed_tab_and_newline_separate_words(self):
        self.assertEqual(word_count("a\tb\r\nc"), 3)


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
