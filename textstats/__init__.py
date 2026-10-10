"""Small text statistics helpers."""

import string
from collections import Counter


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``.

    Tokens made up only of punctuation (``string.punctuation``) are not
    counted. Punctuation attached to a word, as in ``world!``, still counts
    as one word.
    """
    return sum(
        1 for token in text.split() if not all(c in string.punctuation for c in token)
    )


def char_frequency(text: str) -> dict[str, int]:
    """Number of occurrences of each character in ``text``.

    Whitespace characters (those for which ``str.isspace()`` is true) are not
    counted. Matching is case-sensitive, so ``A`` and ``a`` are separate keys,
    and punctuation is counted like any other character.
    """
    return dict(Counter(c for c in text if not c.isspace()))
