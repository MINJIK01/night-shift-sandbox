"""Helpers for detecting secrets in text."""

import re

_SECRET_RE = re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{32,}")


def contains_secret(text: str) -> bool:
    """Whether ``text`` contains an API-key-like string.

    A key is ``sk-`` followed by at least 32 characters from ``[A-Za-z0-9_-]``
    (the prefix is not counted). The ``sk-`` must not be preceded by an
    alphanumeric character, so ``task-...`` is not a match.
    """
    return _SECRET_RE.search(text) is not None
