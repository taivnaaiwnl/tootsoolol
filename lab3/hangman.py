import random
import string

WORDLIST_FILENAME = "data.txt"


def loadWords():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.readline().split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    return all(char in lettersGuessed for char in secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    return ''.join(char if char in lettersGuessed else '_ ' for char in secretWord)


def getAvailableLetters(lettersGuessed):
    return ''.join(letter for letter in string.ascii_lowercase if letter not in lettersGuessed)


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    for mw, ow in zip(my_word, other_word):
        if mw != '_' and mw != ow:
            return False
    return True


def show_possible_matches(my_word):
    wordlist = loadWords()
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print(' '.join(matches))
    else:
        print("No matches found")


def hangman_with_hints(secretWord):
    guesses = 8
    lettersGuessed = []

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    while guesses > 0:
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()

        if guess == "*":
            print("Possible word matches are:")
            show_possible_matches(getGuessedWord(secretWord, lettersGuessed))
            continue

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", end="")
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: ", end="")
        else:
            guesses -= 1
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: ", end="")

        print(getGuessedWord(secretWord, lettersGuessed))

        if isWordGuessed(secretWord, lettersGuessed):
            print("------------\nCongratulations, you won!")
            break

    if not isWordGuessed(secretWord, lettersGuessed):
        print("------------\nSorry, you ran out of guesses. The word was", secretWord + ".")


if __name__ == "__main__":
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman_with_hints(secretWord)
