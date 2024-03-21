import math
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    "*": 0,
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

WORDLIST_FILENAME = "words.txt"


def load_words():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


#
# Problem #1: Scoring a word
#
def get_word_score(word, n):

    word = list(str.lower(word))
    score = []
    for let in word:
        score.append(SCRABBLE_LETTER_VALUES.get(let))
    letter_points = sum(score)

    word_score = 7 * len(word) - 3 * (n - len(word))
    if word_score < 1:
        word_score = 1
    return letter_points * word_score


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line


def deal_hand(n):

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand["*"] = 1
    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):

    new_hand = hand.copy()
    word = str.lower(word)
    for let in new_hand.keys():
        for i in range(len(word)):
            if let in word[i]:
                new_hand[let] = new_hand[let] - 1
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):

    test = []
    test_list = []
    word = str.lower(word)
    word_copy = word
    if "*" not in word:
        for i in range(len(word)):
            if (
                word[i] in hand
                and hand[word[i]] >= word.count(word[i])
                and word in word_list
            ):
                test.append(1)
            else:
                test.append(0)
        if sum(test) == len(word):
            return True
        else:
            return False
    elif "*" in word_copy:
        for i in range(len(VOWELS)):
            if word_copy.replace("*", VOWELS[i]) in word_list:
                test_list.append(1)
                for j in range(len(word_copy)):
                    if word_copy[j] in hand and hand[word_copy[j]] >= word_copy.count(
                        word_copy[j]
                    ):
                        test.append(1)
                    else:
                        test.append(0)
                if sum(test) == len(word_copy):
                    return True
                else:
                    return False
            else:
                test_list.append(0)
        if sum(test_list) != len(VOWELS):
            return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):

    return sum(hand.values())


def play_hand(hand, word_list):

    total_score = 0
    while True:
        if calculate_handlen(hand) == 0:
            print()
            print("Ran out of letters. Total score for this hand:", total_score)
            break
        print()
        print("Current hand:", end=" "), display_hand(hand)
        user_input = str.lower(
            input('Please enter a word, or "!!" to indicate that you are finished: ')
        )
        if user_input == "!!":
            print("Total score for this hand:", total_score)
            break
        else:
            if is_valid_word(user_input, hand, word_list):
                current_word_score = get_word_score(user_input, calculate_handlen(hand))
                total_score = current_word_score + total_score
                hand = update_hand(hand, user_input)
                print(
                    '"%s"' % user_input,
                    "earned",
                    current_word_score,
                    "points. Total:",
                    total_score,
                    "points",
                )
            else:
                print("That is not a valid word. Please choose another word.")
                hand = update_hand(hand, user_input)
    return total_score


def substitute_hand(hand, letter):
    if letter in hand:
        new_hand = hand.copy()
        letter = letter.lower()
        num_letters = new_hand[letter]
        num_vow = math.ceil(num_letters / 3)
        del new_hand[letter]
        while sum(new_hand.values()) < sum(hand.values()):
            for i in range(num_vow):
                x = random.choice(VOWELS)
                if x not in hand:
                    new_hand[x] = new_hand.get(x, 0) + 1
            if sum(new_hand.values()) >= sum(hand.values()):
                break
            for i in range(num_vow, num_letters):
                x = random.choice(CONSONANTS)
                if x not in hand:
                    new_hand[x] = new_hand.get(x, 0) + 1
        return new_hand
    else:
        return hand


def play_game(word_list):
    sub_count = 1
    replay_count = 1
    num_hands = int(input("Enter total number of hands: "))
    TOTAL = 0
    while num_hands >= 1:
        new_score = 0
        hand = deal_hand(HAND_SIZE)
        while sub_count >= 1:
            print()
            print("Current hand:", end=" "), display_hand(hand)
            sub_option = input("Would you like to substitute a letter: ")
            if sub_option.lower() == "yes":
                letter = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter)
                sub_count = sub_count - 1
                break
            elif sub_option.lower() == "no":
                break

        score = play_hand(hand, word_list)

        while replay_count >= 1:
            print("----------")
            replay_option = input("Would you like to replay the hand: ")
            if replay_option.lower() == "yes":
                while sub_count >= 1:
                    sub_option = input("Would you like to substitute a letter: ")
                    if sub_option.lower() == "yes":
                        letter = input("Which letter would you like to replace: ")
                        hand = substitute_hand(hand, letter)
                        sub_count = sub_count - 1
                        break
                    elif sub_option.lower() == "no":
                        break
                new_score = play_hand(hand, word_list)
                replay_count = replay_count - 1
            elif replay_option == "no":
                break

        TOTAL = max(score, new_score) + TOTAL
        num_hands = num_hands - 1
    print("----------")
    print("Total score over all hands: ", TOTAL)


if __name__ == "__main__":
    word_list = load_words()
    play_game(word_list)
