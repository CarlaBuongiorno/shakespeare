import string


def rude_words(sonnets, target_words):
    cleaned_sonnets = ''.join(ch for ch in sonnets if ch not in string.punctuation)
    sonnets_list = [word.lower() for word in cleaned_sonnets.split()]
    for word in target_words:
        is_used = sonnets_list.count(word)
    return f'{word}: {is_used}'
