from settings import Settings
from random import choice
from art import tprint

settings = Settings()

word_set1 = settings.words["easy"]
word_set2 = settings.words["medium"]
word_set3 = settings.words["hard"]


def welcome():
    tprint("Welcome to Hangman Game")

    condition = int(input("1. Play Game\n2. Edit Settings\nSelect an Option (1/2) - "))
    if condition == 1:
        game()
    else:
        settings_key()


def settings_key():
    setting_input = None
    while not setting_input:
        try:
            setting_input = int(
                input(
                    "1. Enter 1 to change the number of turns\n2. Change the difficulty level\n3. Add a word to our dictionary\nSelect an option (1/2/3) - "
                )
            )
            if setting_input not in [1, 2, 3]:
                setting_input = None
                raise ValueError
        except ValueError:
            print("Enter from 1,2,3 only")
    if setting_input == 1:
        settings.change_turns()
    elif setting_input == 2:
        settings.change_level()
    else:
        settings.custom_wordset()
    welcome()


def game():
    if settings.level == 1:
        ogword = choice(word_set1)

    elif settings.level == 2:
        ogword = choice(word_set2)

    else:
        ogword = choice(word_set3)
    word = ogword
    string = []
    turns = settings.turns
    while True:
        for i in word:
            string.append("_")

        while turns > 0:
            if "_" in string:
                letter = input("Guess a letter - ")
                try:
                    x = int(letter)
                    print("Enter only alphabets")
                    continue
                except:
                    pass
                if len(letter) == 1:
                    if letter in word:
                        string[word.index(letter)] = letter
                        word = word.replace(letter, "_", 1)
                        print("Correct!")
                        print("".join(string))

                    else:
                        turns -= 1
                        print("Turns left- " + str(turns))
                else:
                    print("Enter only one alphabet")
            else:
                print("Congratulations! The correct answer is " + "".join(string))
                break

        if turns == 0 and "_" in string:
            print("".join(string))
            guessword = input("Guess the word?")
            if guessword == ogword:
                print("Congratulations!,the correct answer is " + ogword)
            else:
                print("wrong!,the correct answer is " + ogword)

        replay = input("Do you want to play again?(yes/no)")
        if replay.lower() == "no":
            welcome()
        else:
            game()


welcome()
