from temp import sub_and_word_count
import pytest


@pytest.mark.parametrize('x, y, expected',
                         [
                             (3, 4, -1),
                             (4.5, 4, 0),
                             (3.9, 4, -1),
                             (4.2, 3.9, 0)
                         ])
def test_sub_parametrize(x, y, expected):
    assert sub_and_word_count.sub(x, y) == expected


@pytest.mark.parametrize('sentence, word, expected_count',
                         [
                             ('arm pod race', 'pod', 1),
                             ('arm pod race', 'lap', 0),
                             ('arm arm arm', 'arm', 3),
                         ])
def test_word_count(sentence, word, expected_count):
    assert sub_and_word_count.word_count(sentence, word) == expected_count
