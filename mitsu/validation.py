#!/usr/bin/env python3

import re
import sys


def is_palindrome(text: str) -> bool:
    """Determine whether the given text is a palindrome

    Ignores all punctuation, whitespace and upper/lower case.

    :param text: The text to examine
    :return: ``True`` if the text is a palindrome

    """
    letters = list(re.findall(r'\w', text.lower()))
    backwards = list(reversed(letters))
    return letters == backwards


def is_palindrome_cmd():
    """Entry point for the ``is_palindrome`` command line utility

    Usage::

        is_palindrome This is not a palindrome.

    Exits with a zero return value if the text from all arguments form a
    palindrome, or 1 if it doesn't.

    """
    text = ' '.join(sys.argv[1:])
    if is_palindrome(text):
        sys.exit(0)
    else:
        print(f'Is NOT a palindrome: {text}')
        sys.exit(1)
