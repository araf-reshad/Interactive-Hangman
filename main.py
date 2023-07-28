import random

def found(letter, word): #define a new function that returns True if a certain letter is found within a word, or False otherwise
  
    for x in word:
      
        if x == letter:
          
            return True
          
    return False

print("""Welcome to the Hangman Game! 
-------------------------------------------------""")

while True: 
    name = input("Please enter your username here: ")
  
    if name.isalnum() == True:  #checks if name only has letters and numbers
        print("\nHi", name, "glad to have you here!")
      
        break  

    else:  
        print("\nPlease enter your name using letters and numbers only\n")

#using triple quotes to have a multi-line print statement
#explains the rules of the game
print("""-------------------------------------------------
The rules of the game are as follows:

Say hello to your friend Mr. Minion.

  ㋡
--│--
  │
 / \\ 
 
Guess the secret word in 7 tries or less to keep Mr. Minion alive!""")


tries = 7 #the number of tries left

ans_list = ['computer', 'input', 'variable', 'float', 'integer', 'function', 'modulo','runtime', 'boolean', 'parameter']

ans_word = random.choice(ans_list)

hangman = [' ___\n|   |\n', '㋡  |\n', '\\', '|', '/ |\n', '/ ', '\ |\n    |'] # list that stores the different 'limbs' of the hangman


guess = "" #a string that will store the letters guessed by the player

while tries > 0:
    print("\n-------------------------------------------------")

  
    user_input = input("\nDo you want a hint? It will cost you 2 tries! (You have " + str(tries) +  " remaining)\n\nType 'Help' for a hint, anything else to continue as usual.\n\n") 

    if user_input.lower() == 'help':  #any capitalization of "help" will trigger the hint  
      
      hint = random.choice(ans_word) #pick a random letter in the word as the hint

      while found(hint, guess) or not found(hint, ans_word): #if the letter has already been guessed, choose the nearest letter
        
        if hint=='z':
          
          hint = 'a'
          
        else:
          
          hint = chr(ord(hint) + 1)
          
      print('\nAs you wish. Your hint is \"' + hint + "\"\n")
      
      user_input=hint

      
      tries -= 2 #2 tries are deducted for using the hint 

      if not tries: #if the user runs out of tries, quit the game
        
        break

    
    else: #user is asked to enter a letter if they don't want a hint

      user_input = "#"

      print('\nThe game continues.')
      
      while True: #keep prompting user if given invalid input
        
        user_input = input("\nEnter a letter: ")

        user_input = user_input.lower()
  
        print()

        if (len(user_input) > 1 or user_input < 'a' or user_input > 'z'): #checks if the letter is valid (an alphabetic character of length 1)
            print("Invalid guess. Try again.")
          
            continue 
          
        if found(user_input, guess):
            print("You have already guessed this before. Try again.")
          
            continue
          
        break
      

    guess += user_input #adds the current letter to the string of letters guessed

    if not found(user_input, ans_word):
        print("Wrong guess. Mr Minion's suffering continues.\n")
        
        tries -= 1

    else:
        print("Good job! Mr Minion heaves a sigh of relief.\n")

    print("You have", max(0, tries), "tries left.\n") #tries cannot be negative

    print("The word is: ", end="")

   
    whole_word = True #boolean variable to check if the user has guessed the whole word

    for letter in ans_word: 
        if (found(letter, guess)):
            print(letter, end=' ') #if the letter has been guessed, print the letter

        else: #if the letter has not been guessed, hide the letter
            print("_ ", end='')
            whole_word = False  #keep track that the user has not guessed the whole word

    print()

    for i in range(min(7, 7 - tries)):  #print the corresponding number of limbs of the hangman
        print(hangman[i], end="")

    print()

    if whole_word:
        print("""\nCongrats! You have saved Mr. Minion!
 
 😊   
--│--     
  │   
 / \   """)
      
        break  #exit the game

    if tries <= 0:   #if the user runs out of tries
        print("\nBetter luck next time. The word was \"" + ans_word +
              """\". RIP Mr. Minion.
              
 😢    
--│-- 
  │  
 / \ """)
    