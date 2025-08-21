'''
Write a program to report on how many rude words Shakespeare ever used, i.e.:

"fuck": 3
"shit": 9
"piss": 0
"zounds": 3

(I don't know what the actual numbers would be, you'll find out!) https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'''

import requests

from shakespeare import rude_words


def main():
    url = 'https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'
    r = requests.get(url)
    sonnets = r.text
    target_words = ["fuck", "shit", "piss", "zounds"]
    rude_word_count = rude_words(sonnets, target_words)
    for rude_word in rude_word_count:
        print(f'{rude_word[0]}: {rude_word[1]}')


if __name__ == '__main__':
    main()
