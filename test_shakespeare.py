from shakespeare import rude_words


def test_rude_words_function_exists():
    assert rude_words


def test_split_sonnets():
    sonnets = 'This is a sonnet.'
    assert rude_words(sonnets) == ['This', 'is', 'a', 'sonnet.']