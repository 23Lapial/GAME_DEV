import random
import time

with open('words', mode='r') as f:
    word_list = f.read().split()
word = random.choice(word_list)

base = ['_' for character in word]
full_word = [character for character in word]


def load_word():
    for index, character in enumerate(full_word):
        if random.choice(full_word) in full_word[index]:
            base[index] = character
            print(' '.join(base))
            time.sleep(2)


if __name__ == '__main__':

    while True:
        load_word()
