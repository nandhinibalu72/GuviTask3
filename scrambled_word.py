#importing random inbuilt library from python
import random
print("Welcome to the scrambled word game. Let's start")
 #initializing the words in list
words=['python','javascript','java','automation','pytest','guvi','selenium']
 # picking up a random word to scramble 
original_word= random.choice(words) 
 #scrambling the selected word using random sample
scrambled_word=''.join(random.sample(original_word,len(original_word))) 
print(f"scrambled_word :{scrambled_word}")
 # Game loop 
while True:
     user_guess=input("Guess the word: ").lower()
     #verifying user input matches with original word. 
     if user_guess==original_word:
         print("congratulations, you guessed it ")
         break
     else:
         print("Wrong guess, Try again!")