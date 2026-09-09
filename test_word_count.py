from word_count import count_words


def test_count_words_basic():
    assert count_words("hello world") == 2


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_extra_whitespace():
    assert count_words("  hello   world  ") == 2
