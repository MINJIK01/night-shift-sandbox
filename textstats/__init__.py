"""Small text statistics helpers: word_count, char_frequency, bar_chart and
visualize_chars."""

import string
import unicodedata
from collections import Counter


def _is_punctuation(char: str) -> bool:
    return char in string.punctuation or unicodedata.category(char).startswith("P")


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``.

    Tokens made up only of punctuation (``string.punctuation`` or any
    Unicode punctuation category ``P*``) are not counted. Punctuation attached to
    a word, as in ``world!``, still counts as one word. Symbols (Unicode category
    ``S*``, such as ``€`` or ``→``) are not punctuation, so a token made up only
    of symbols is counted as a word.
    """
    return sum(1 for token in text.split() if not all(_is_punctuation(c) for c in token))


def char_frequency(text: str) -> dict[str, int]:
    """Number of occurrences of each character in ``text``.

    Whitespace characters (those for which ``str.isspace()`` is true) are not
    counted. Matching is case-sensitive, so ``A`` and ``a`` are separate keys,
    and punctuation is counted like any other character.
    """
    return dict(Counter(c for c in text if not c.isspace()))


def bar_chart(counts: dict[str, int], width: int = 40) -> str:
    """Text bar chart of ``counts``, one ``key | ████ value`` line per entry.

    The largest value fills ``width`` cells and the others are scaled in
    proportion. Any value above zero gets at least one cell. Lines are sorted
    by value descending, then key ascending, and keys are padded to the same
    width. An empty ``counts`` gives an empty string. Raises ``ValueError`` if
    ``width`` is below 1 or any value is negative.
    """
    if width < 1:
        raise ValueError("width must be at least 1")
    if any(v < 0 for v in counts.values()):
        raise ValueError("counts must not contain negative values")
    if not counts:
        return ""
    largest = max(counts.values())
    key_width = max(len(k) for k in counts)
    lines = []
    for key, value in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        cells = 0 if value == 0 else max(1, round(value * width / largest))
        lines.append(f"{key.ljust(key_width)} | {'█' * cells} {value}")
    return "\n".join(lines)


def visualize_chars(text: str, top: int | None = None, width: int = 40) -> str:
    """Text bar chart of the character frequencies of ``text``.

    Renders ``char_frequency(text)`` with ``bar_chart``, so whitespace is not
    shown. If ``top`` is given, only the ``top`` most frequent characters are
    kept (ties are broken by character, ascending). Text without visible
    characters gives an empty string. Raises ``ValueError`` if ``top`` is below
    1, or if ``width`` is below 1.
    """
    if top is not None and top < 1:
        raise ValueError("top must be at least 1")
    counts = char_frequency(text)
    if top is not None:
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        counts = dict(ranked[:top])
    return bar_chart(counts, width)
