""""
Theme of my Final Project is "Word Guessing Game"
where the player attempts to build a missing word by guessing one letter at a time.
After a particular number of incorrect guesses, the game ends and therefore the player loses.
The game also ends if the player correctly identifies all the letters of the missing word.

"""

def main():

    word = 'happycoding'
    guesses = 8
    display = '_' * len(word)

    game_over = False

    while not game_over:
        print("You have " + str( guesses ) + " guesses " + "left")
        print("The word now looks like this: " + display)
        guess = input("Type a single letter here, then press enter: ")

        i = 0
        if guess in word:
            while word.find(guess, i) != -1:
                i = word.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            print("Correct!")
        else:
            print("Sorry, wrong guess.")
            guesses -= 1

        if guesses == 0:
            print("Sorry, you lost. The secret word was: " + word)
            game_over = True
        if word == display:
            print("Congratulations, the word is: " + word)
            print("Thank you for playing word guessing game")
            game_over = True

if __name__ == '__main__':
    main()

