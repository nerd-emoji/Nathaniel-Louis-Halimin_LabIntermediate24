life = 6
secretLetter = 'z'
guessed = {}
while life > 0:
    new = False
    guess = input("Guess the secret letter you have "+str(life)+" lives left")
    if guess == secretLetter:
      print("you got it")
      break
    elif guess != secretLetter:
       for x in guessed:
           if guess == x:
               print("test")
               new = True
               print("you have already guessed that letter")
               break
       if new == False:
           life -= 1
           guessed[guess] = True
           print("Wrong Guess")
if life == 0:
    print("You ran out of lives") 
       