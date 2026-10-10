"""Small text statistics helpers."""

import string
import unicodedata
from collections import Counter


def _is_punctuation(char: str) -> bool:
    return char in string.punctuation or unicodedata.category(char).startswith("P")


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``.

    Tokens made up only of punctuation (``string.punctuation`` or any
    Unicode punctuation category ``P*``) are not counted. Punctuation attached to a word, as in ``world!``, still counts
    as one word.
    """
    return sum(1 for token in text.split() if not all(_is_punctuation(c) for c in token))


def char_frequency(text: str) -> dict[str, int]:
    """Number of occurrences of each character in ``text``.

    Whitespace characters (those for which ``str.isspace()`` is true) are not
    counted. Matching is case-sensitive, so ``A`` and ``a`` are separate keys,
    and punctuation is counted like any other character.
    """
    return dict(Counter(c for c in text if not c.isspace()))
