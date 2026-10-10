"""Small text statistics helpers."""

import string


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``.

    Tokens made up only of punctuation (``string.punctuation``) are not
    counted. Punctuation attached to a word, as in ``world!``, still counts
    as one word.
    """
    return sum(
        1 for token in text.split() if not all(c in string.punctuation for c in token)
    )
