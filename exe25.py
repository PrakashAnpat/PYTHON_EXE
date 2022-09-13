def break_words(stuff):
    words = stuff.split(" ")# split() method is used to split/break a string into pieces.This pieces returns as a list.
    return words

def sort_words(words):
    return sorted(words)# sorted() function returns sorted list of the specified iterable object.

def print_first_word(words):
    word = words.pop(0)# pop() method delete element of the specifed position number & returns it.
    print("Returned first element:-",word) # deleted element.

def print_last_word(words):
    word = words.pop(-1)
    print("Returned last element:-",word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print(words)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
