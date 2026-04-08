import pytest
from main import count_words, count_sentences


@pytest.fixture
def simple_text():
    return "Hello world. How are you? I am fine!"


@pytest.fixture
def empty_text():
    return ""


@pytest.mark.parametrize("text, expected", [
    ("Hello world", 2),
    ("one, two; three: four", 4),
    ("word", 1),
    ("Hello world. How are you?", 5),
])
def test_count_words(text, expected):
    assert count_words(text) == expected


def test_count_words_simple(simple_text):
    assert count_words(simple_text) == 8


def test_count_words_empty(empty_text):
    assert count_words(empty_text) == 0


@pytest.mark.parametrize("text, expected", [
    ("Hello world. How are you? I am fine!", 3),
    ("One sentence.", 1),
    ("Wait... Really! Yes?", 3),
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


def test_count_sentences_simple(simple_text):
    assert count_sentences(simple_text) == 3


def test_count_sentences_empty(empty_text):
    assert count_sentences(empty_text) == 0
    