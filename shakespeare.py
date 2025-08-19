def rude_words(sonnets, target_words):
    sonnets_list = sonnets.split()
    sonnets_list = [word.lower() for word in sonnets_list]
    for word in target_words:
        print(word)
        is_used = sonnets_list.count(word)
    return f'{word}: {is_used}'
