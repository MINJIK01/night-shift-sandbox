import unittest

from textstats.secrets_check import contains_secret


class ContainsSecretTest(unittest.TestCase):
    def test_exact_length(self):
        self.assertTrue(contains_secret("sk-" + "a" * 32))

    def test_too_short(self):
        self.assertFalse(contains_secret("sk-" + "a" * 31))

    def test_in_sentence(self):
        self.assertTrue(contains_secret("my key is sk-" + "A1b2" * 8 + " ok"))

    def test_after_equals(self):
        self.assertTrue(contains_secret("key=sk-" + "a" * 40))

    def test_empty_and_plain(self):
        self.assertFalse(contains_secret(""))
        self.assertFalse(contains_secret("just a normal sentence"))

    def test_prefix_part_of_word(self):
        self.assertFalse(contains_secret("task-" + "a" * 40))


if __name__ == "__main__":
    unittest.main()
