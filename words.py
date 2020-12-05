import random
class random_word_picker:
    def __init__(self):
        words = ["hello", "beutiful", "color", "there"]
        guess_word = random.choice(words)
        return guess_word