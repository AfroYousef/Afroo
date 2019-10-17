from collections import Counter
import os
from termcolor import colored

def green(word):
    word = str(colored(word, 'green'))
    return word
def red(word):
    word = str(colored(word, 'red'))
    return word
def yellow(word):
    word = str(colored(word, 'yellow'))
    return word
def orange(word):
    word = str(colored(word, 'orange'))
    return word
def black(word):
    word = str(colored(word, 'black'))
    return word

def diflet(string, start=''):
    if start == '':
        start = 0
    string = str(string)
    for char in str(Counter(string)):
        if char == "'":
            start += 0.5
    return int(start)

def vsco(worrrrrrd):
    worrrrrrd += 'sksksksksksksksksksksksksks'
    return worrrrrrd
