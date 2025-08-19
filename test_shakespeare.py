from shakespeare import rude_words


def test_rude_words_function_exists():
    assert rude_words


def test_count_target_word():
    sonnets = 'This is a sonnet.'
    assert rude_words(sonnets, ['a']) == f'a: 1'


def test_target_word_has_capitals():
    sonnets = 'This is A sonnet.'
    assert rude_words(sonnets, ['a']) == f'a: 1'


def test_target_word_has_punctuation():
    sonnets = 'This is A sonnet.'
    assert rude_words(sonnets, ['sonnet']) == f'sonnet: 1'
