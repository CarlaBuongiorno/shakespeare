def rude_words(sonnets, target_words):
    sonnets_list = sonnets.split()
    for word in target_words:
        used = sonnets_list.count(word)
    return f'{word}: {used}'
