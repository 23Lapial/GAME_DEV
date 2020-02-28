import random

with open('words', mode='r') as f:
    word_list = f.read().split()
word = random.choice(word_list)


letters_in_word = ['_' for character in word]
characters_in_word = [character for character in word]
letters_guessed = []


def display(geuss):

    for index, letter in enumerate(characters_in_word):
        if geuss == characters_in_word[index]:
            letters_in_word[index] = letter

    print(letters_in_word)


def geuss():

    letter = str(input())
    return letter


if __name__ == '__main__':

    while True:
        display(geuss())
