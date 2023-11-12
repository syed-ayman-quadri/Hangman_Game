'''
Author: Syed Ayman Quadri
Date: November 12, 2023
Summary: This is a simple hangman game.

Detail: This game picks a random word and displays the first and last letters.
        Then the user guesses the remaining letters.
        The user gets 7 tries to guess the correct letters. For every wrong guess, the user loses tries.
        If the user guesses a correct letter and the letter appears more than once, then all the occurrences
        of the letter get filled.
        If the user successfully guesses all the letters before their tries run out, they win.
        Otherwise the correct letter is displayed and they lose.
'''

import random as rm
import string
from copy import deepcopy


def Database():
    '''
    This contains a list of words to be used when the game runs. The functions return the list of words.
    '''
    words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot',
             'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 
             'muskmelon']
    return words


def GetRandomWord(data):
    '''
    This functions takes in a list containing many words. The function chooses a random word from the list
    and return it as a string.
    '''
    word = rm.choice(data).strip().lower()
    return word


def DisplayWord(UserWordList):
    '''
    This function takes a list and displays the individual characters.
    If the user has not already guessed the letters, then '_' is displayed.
    '''
    for chr in UserWordList:
        if chr != 0:
            print(chr, end=' ')
        else:
            print(f"_", end=' ')
    print()


def UserGuess():
    '''
    This function asks the user for a letter as a guess.
    If the letter input is not valid, it asks the user again until it's correct.
    '''
    while True:
        try:
            guess = input(f"Enter a letter to guess: ").strip().lower()
            if guess not in string.ascii_letters:
                raise Exception
            return guess
        except:
            print("Please enter a valid letter.")


def main():
    database = Database()
    word = GetRandomWord(database)

    # Random word in the list format
    wordList = []
    for chr in word: wordList.append(chr)
    CopyWordList = deepcopy(wordList)
    CopyWordList.pop(0)
    CopyWordList.pop(-1)

    # List contains a 0 in the places where the user has not guessed anything
    UserWordList = []
    UserWordList.extend([0] * len(wordList))
    UserWordList[0] = wordList[0].upper()
    UserWordList[-1] = wordList[-1]

    print(f"Guess the word! HINT: word is the name of a fruit")

    win = False
    lose = False
    tries = 7

    while win == False and lose == False:
        DisplayWord(UserWordList)

        guess = UserGuess()

        # Updating UserWordList when guess is correct even if the guessed letter is present multiple times
        if guess in CopyWordList:
            for i in range(len(wordList)):
                if guess == wordList[i]:
                    UserWordList[i] = guess
        else:
            # Losing tries when guess is wrong or the same letter is guessed again
            tries -= 1

        if 0 not in UserWordList:
            DisplayWord(UserWordList)
            print(f"Congrats !! You Won 🎉🎉\nThe final word is {word}.")
            win = True
        elif tries == 0:
            print(f"Sorry, you've run out of tries 😞. Better luck next time.\nThe word was {word}.")
            lose = True


if __name__ == '__main__':
    main()