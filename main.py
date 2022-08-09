import random


def guess_word():
    word = random.choice(words)
    print("Guess the word")
    return word


def is_present(letter):
    if letter.lower() in word.lower():
        return letter.lower()
    else:
        return False


def fill(letter):
    global dash, word
    dash = list(dash)
    for i, l in enumerate(word):
        if letter == l:
            dash[i] = letter
            print("".join(dash))


def make_hangman():
    global chances
    chances = chances + 1
    print(hangman[chances])


def check_letter(user_choice):
    letter = is_present(user_choice)
    if letter:
        fill(letter)
    else:
        make_hangman()


hangman = [
    '''
-------
   |
   |
   |
 =====''', '''
-------
 O |
   |
   |
 =====''', '''
-------
 O |
 | |
   |
 =====''', '''
-------
 O |
/| |
   |
 =====''', '''
-------
 O |
/|\|
   |
 =====''', '''
-------
 O |
/|\|
/  |
 =====''', '''
-------
 O |
/|\|
/ \|
 ====='''
]
chances = 0
is_win = False
words = [
    "classic", "rate", "crown", "book", "page", "bench", "classmate", "bench",
    "letter", "text", "table", "chair", "pen", "pencil", "eraser", "box",
    "sharpner", "bottle", "lunch", "water", "student", "teacher", "stick",
    "paper", "bag", "food", "tea", "speaker", "microphone", "ink", "uniform",
    "window", "door"
]
word = guess_word()
dash = "_" * len(word)
print(dash)
print(hangman[0])

while chances <= 5:
    user_choice = input()
    check_letter(user_choice)
    if "_" not in dash:
        is_win = True
        break

if is_win:
    print("Win")
else:
    print("Lost")
