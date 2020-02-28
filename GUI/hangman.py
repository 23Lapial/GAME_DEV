import random
import time

# opens word.txt and picks a random word
with open('words', mode='r') as f:
    word_list = f.read().split()
word = random.choice(word_list)

base_word = ['_' for character in word]
full_word = [character for character in word]


def hangman(letter):

    global guesses

    for index, character in enumerate(full_word):
        if letter in full_word[index]:
            base_word[index] = character

    if letter not in full_word:
        guesses -= 1

    print(' '.join(base_word))

    return letter == ''.join(full_word)


# amount of guesses
guesses = len(word) + 5


def guess():
    letter = str(input())
    return letter


def check_winner():
    return full_word[:] == base_word[:]


game_active = True

print(' '.join(base_word), f'WORDS: {len(word)}')

while __name__ == '__main__':

    while game_active:

        # win if user entered word(anytime)
        if hangman(guess()):
            print('\nYOU GUESSED THE WORD!\nThe word was,', ''.join(full_word))
            game_active = False

        print(f'GUESSES: {str(guesses)}')

        # if user guess all letters
        if check_winner():
            print('\nYOU GUESSED IT!\nThe word was,', ''.join(full_word))
            game_active = False

        # win if user entered word(end)
        if guesses == 0:
            word_guess = str(input('Guess the word: '))
            if word_guess == ''.join(full_word):
                print('YOU GUESSED THE WORD!')
                game_active = False
            else:
                print('\nYOU DID NOT GUESS IT!\nThe word was,', ''.join(full_word))
                game_active = False
