import random
from string import ascii_lowercase
list1 = ['python', 'java', 'kotlin', 'javascript']

print('H A N G M A N')
choice = choice = input("Type \"play\" to play the game, \"exit\" to quit: ")


while choice == "play":
    word = random.choice(list1)
    hiddenString = []
    guess_list = []
    attempts = 8

    for char in word:
        hiddenString.append("-")    

    while attempts > 0:
        print()
        print(''.join(hiddenString))
        guess = input("Input a letter: ")
        if len(guess) > 1:
                print("You should input a single letter")
        elif guess not in ascii_lowercase:
                print("It is not an ASCII lowercase letter")
        elif guess in guess_list:
            print("You already typed this letter")
        elif guess in hiddenString:
                print("No improvements")
                attempts -= 1
        elif guess not in word:
            print("No such letter in the word")
            attempts -= 1
        if guess in word:

            for i in range(len(word)):
                char = word[i]
                if char == guess:
                    #print()
                    hiddenString[i] = word[i]


        guess_list.append(guess)

        if  hiddenString == list(word):
            print(f"You guessed the word {word}!")
            print("You survived!\n")
            choice = input("Type \"play\" to play the game, \"exit\" to quit: ")
            break
            
        elif attempts == 0:
            print("You are hanged!\n")
            choice = input("Type \"play\" to play the game, \"exit\" to quit: ")
            break
