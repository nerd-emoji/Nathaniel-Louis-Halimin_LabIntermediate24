secretWord = "bee"
guess = False
while guess == False:
    word = input("Enter a word: ")
    if word == secretWord:
        print("You win")
        guess = True
    else:
        print("try again")