import pytest
import string

def remove_punctuation(texts):
    result = []
    for text in texts:
        punctuation_count = sum(1 for char in text if char in string.punctuation)
        text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
        result.append((punctuation_count, text_without_punctuation))
    return result

@pytest.mark.parametrize("texts, expected", [
    (["Hello, world!", "This is a test."], [(2, "Hello world"), (1, "This is a test")]),
    (["Foo, bar, baz!", "Qux, quux, corge."], [(3, "Foo bar baz"), (3, "Qux quux corge")]),
    (["No punctuation here"], [(0, "No punctuation here")]),
])
def test_remove_punctuation(texts, expected):
    assert remove_punctuation(texts) == expected
