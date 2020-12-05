import time
import random
import words

name = input("Enter your name: ")
print("Hello! " + name + " Welcome to HangMan game")
time.sleep(1)
guess_count = 10
guess_word = "secret"
print(guess_word)
while (guess_count > 0):
    user_word = input("enter your Guess: ")
    if user_word == guess_word:
        time.sleep(1)
        print("you won! ")
        break
    else:
        guess_count = guess_count - 1
        time.sleep(1)
        print("wrong guess! ")
        print("you have", + guess_count, "left")
if guess_count == 0:
    time.sleep(1.5)
    print("you lost")
