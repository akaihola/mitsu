from typing import Tuple

import pytest

from mitsu import mirror


def extract(text: str, divider: str) -> Tuple[str, int]:
    divider_pos = text.index(divider)
    before_cursor = text[:divider_pos]
    after_cursor = text[divider_pos + 1:]
    return f'{before_cursor}{after_cursor}', divider_pos


def inject(text: str, position: int, divider: str) -> str:
    before_cursor = text[:position]
    after_cursor = text[position:]
    return f'{before_cursor}{divider}{after_cursor}'


@pytest.mark.parametrize(
    'before, after, expect',
    [('|', '_|', '_|'),
     ('|', 'a_|', 'a_|'),
     ('|', 'ab_|', 'ab_|'),
     ('a|', '_|', '_|'),
     ('a|', 'a_|', 'a_|'),
     ('a|', 'aa_|', 'aa_|a')
    ]
)
def test_mirror_changes(before, after, expect):
    before_text, before_midpoint = extract(before, '|')
    after_text, after_cursor = extract(after, '_')

    result_text, result_cursor = mirror.mirror_changes(before,
                                                       after_text,
                                                       after_cursor)

    result = inject(result_text, result_cursor, '_')
    assert result == expect
