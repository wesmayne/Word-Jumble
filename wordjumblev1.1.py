#wordjumblev1.1 - Player has to guess a random word from dictionary, if player fails they can 'cheat' and get the word

import urllib.request
import random


word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
WORDS = long_txt.splitlines()

print("Welcome to Wes's Word Jumble Game!\n")
input("Press Enter to begin")
def game():
    word = random.choice(WORDS)
    correct = word
    jumble = ''
    attempts = 1
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position]+word[(position + 1):]
    print ("\nYour word is: ", jumble,'\n')

    guess = input("Your Guess: ")
    #guess = guess.lower()
    while (guess != correct):
        attempts +=1
        print("Incorrect")
        cheat = input("Would you like to cheat? (y/n)")
        if cheat == 'y':
            print(correct)
        elif cheat != 'n':
            print("Invalid Response\n")
        guess = input("Your Guess: ")
        #guess = guess.lower()
    if guess == correct and cheat =='y':
        print("Well your a dirty cheater so you deserve nothing")
    if guess == correct and cheat != 'y':
        print("Congrats! You guessed it in ", attempts, "tries")

game()
replay = input("Would you like to play again? (y/n)")
while replay == 'y':
    game()
    replay = input("Would you like to play again? (y/n)\n")
print("\nThanks for playing!")


