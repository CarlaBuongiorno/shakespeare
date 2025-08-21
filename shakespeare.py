import string


def rude_words(sonnets, target_words):
    cleaned_sonnets = ''.join(ch for ch in sonnets if ch not in string.punctuation)
    sonnets_list = [word.lower() for word in cleaned_sonnets.split()]
    is_used = [(word, sonnets_list.count(word)) for word in target_words]
    return is_used
