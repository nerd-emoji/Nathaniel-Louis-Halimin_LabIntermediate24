'''
def main(sWord):
    print("Welcome to Hangman! Your objective is to find the secret word by guessing one letter at a time.")
    print("You have 5 lives, if you run out you lose.")
    print("Good luck!")
    allGuessWords = ""
    lives = 5
    win = False
    while lives > 0:
        if win == True:
            print("Congratulations! You won!")
            break
        guessWord = input("Guess a letter: ")
        allGuessWords += guessWord
        lives, win = updateText(allGuessWords, sWord, guessWord, lives, win)
    
    if lives == 0:
        print("You lose! The secret word was", sWord)


def updateText(allGuessWords, sWord, guessWord, lives, win):
    win = True
    for letter in sWord:
        if letter in allGuessWords:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            win = False
    
    if guessWord in sWord:
        print("Congrats,", guessWord, "is in the secret word!")

    elif guessWord not in sWord:
        lives -= 1
        print("Incorrect! You have", lives, "lives left.")

    return lives, win
        

sWord = str(input("Enter the secret word: "))
main(sWord)
'''
import random
wins = 0
losses = 0
def main():
    sWordList = ["apple", "banana", "cherry"]
    print("Welcome to Hangman! Your objective is to find the secret word by guessing one letter at a time.")
    print("You have 5 lives, if you run out you lose.")
    print("Good luck!")
    for i in range(len(sWordList)):
        sWord = random.choice(sWordList)
        allGuessWords = ""
        lives = 5
        win = False
        gameRound(allGuessWords, sWord, lives, win)
        sWordList.remove(sWord)
        print("Do you want to continue playing?, y for yes, n for no")
        answer = input()
        if answer == "y":
            continue
        elif answer == "n":
            break
    print("Wins:", wins, "Losses:", losses)

def gameRound(allGuessWords, sWord, lives, win):
            global wins
            global losses
            for letter in sWord:
                print("_", end=" ")
            while lives > 0:
                if win == True:
                    print("Congratulations! You won!")
                    wins += 1
                    break
                guessWord = input("Guess a letter: ")
                allGuessWords += guessWord
                lives, win = updateText(allGuessWords, sWord, guessWord, lives, win)
                if lives == 0:
                    print("You lose! The secret word was", sWord)
                    losses += 1
                    break

def updateText(allGuessWords, sWord, guessWord, lives, win):
    win = True
    for letter in sWord:
        if letter in allGuessWords:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            win = False
    
    if guessWord in sWord:
        print("Congrats,", guessWord, "is in the secret word!")

    elif guessWord not in sWord:
        lives -= 1
        print("Incorrect! You have", lives, "lives left.")
    return lives, win     
main()