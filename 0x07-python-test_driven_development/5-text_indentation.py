#!/usr/bin/python3

def text_indentation(text):
    """Function that prints indentation"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    words = text.split()
    words_with_newline = []

    for word in words:
        if ("?" in word or ":" in word or "." in word):
            word = word + '\n \n'
            words_with_newline.append(word)
        else:
            words_with_newline.append(word + ' ')

    print(''.join(words_with_newline))
