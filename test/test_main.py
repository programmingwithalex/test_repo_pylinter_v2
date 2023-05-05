import main
import pytest


def test_add():
    assert main.add(3, 4) == 7
    assert main.add(3.5, 4) == 7
    assert main.add(3.9, 4) == 7
    assert main.add(3.9, 4.1) == 8


@pytest.mark.parametrize('x, y, expected', [
    (3, 4, 7), 
    (3.5, 4, 7),
    (3.9, 4, 7),
    (3.9, 4.1, 8)
    ])
def test_add_param(x, y, expected):
    assert main.add(x, y) == expected


def test_to_sentence():
    assert main.to_sentence('apple') == 'Apple.'
    assert main.to_sentence('Apple trees') == 'Apple trees.'
    assert main.to_sentence('Apple trees.') == 'Apple trees.'


@pytest.mark.parametrize('sentence, expected', [
            ('apple', 'Apple.'),
            ('apple trees', 'Apple trees.'),
            ('Apple trees.', 'Apple trees'),
        ]
)
def test_sentence_parametrize(sentence, expected):
    assert main.to_sentence(sentence) == expected
                              