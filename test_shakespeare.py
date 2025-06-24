from shakespeare import rude_words


def test_rude_words_function_exists():
    assert rude_words


def test_count_target_word():
    sonnets = 'This is a sonnet.'
    assert rude_words(sonnets, 'a') == f'a: 1'