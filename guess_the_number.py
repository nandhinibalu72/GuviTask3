#importing random inbuilt library from python
import random
print("Let's play a number guesssing game from the range of 20 to 40. Let's start")
 #intializing random range of numbers from 20 to 30
random_number_to_guess=random.randint(20,40)
 #initializing while to verify the user guess match with random number generated.
while True:
     #get the input from user to guess the value
     guess_of_user=int(input("Enter a number to guess the value: "))
     #Verifying if user guess is less than random number printing Too low as output
     if guess_of_user < random_number_to_guess: 
         print("Too low, try again")
     #Verifying if user guess is greater than random number printing Too high as output
     elif guess_of_user > random_number_to_guess:
         print("Too high, Try again")
     #Verifying if user guess is match with random number printing as Correct guess output
     else:
         print(f"Correct guess, The number is {random_number_to_guess} congratulations")
         break