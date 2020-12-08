from words import word_list
import random
from display_hangman import display_hangman

def Random_word():
    guess_word = random.choice(word_list)
    return guess_word.upper()

def Play():
    guess_word = Random_word()
    word_length = "__ " * len(guess_word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    guess_count = 6
    print("\n")
    name = input("Enter Your name: ")
    print("Hello " + name.upper() + " welcome to the Hangman_World!")
    print(display_hangman(guess_count))
    print(word_length)
    while not guessed and guess_count > 0:
        user_word = input("Enter your guess: ").upper()
        if len(user_word) == 1 and user_word.isalpha():
            if user_word in guessed_letters:
                print("you alreday guessed the letter")
            elif user_word not in guess_word:
                print(user_word, " not in the word")
                guess_count -= 1
                guessed_letters.append(user_word)
                print(display_hangman(guess_count))
            else:
                print("well done, " + user_word + " is in the word")
                guessed_letters.append(user_word)
        elif len(user_word) == len(guess_word) and guess_word.isalpha():
            if user_word == guess_word:
                print("Wow! correct Guess, Well done")
                break
            else:
                print("your guess is Wrong!")
                guessed_word.append(user_word)
                guess_count -= 1
                print(display_hangman(guess_count))
        else:
            print("wrong guess")
            guessed_word.append(user_word)
            guess_count -= 1
            print(display_hangman(guess_count))
    play_again()

def play_again():
    replay = input("play again! Y/N : ").upper()
    if replay == "Y":
        main()

def main():
    Random_word()
    Play()

main()

