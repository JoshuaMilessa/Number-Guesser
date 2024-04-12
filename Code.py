import random

guesses = 0  # Initialize guesses counter

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

top_of_rang = input("Type a number: ")

if top_of_rang.isdigit():
  top_of_rang = int(top_of_rang)

  if top_of_rang <= 0:
    print("Please type a number larger than 0 next time.")
    quit()

else: 
  print("Please type a number next time.")
  quit()
  
random_number = random.randint(0, top_of_rang)

while True:
  guesses += 1
  user_guess = input("Make a guess: ")
  if top_of_rang.isdigit():
   user_guess = int(user_guess)

  else:
    if int(user_guess) > random_number:
      print("You were above the number!")
    else:
      print("You were below the number!")

  if user_guess == random_number:
    print("You got it!")
    break
  else:
    print("You got it wrong!")
    
print("You got it in ", guesses, " guesses")


