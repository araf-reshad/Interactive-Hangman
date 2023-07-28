**Goal:** 

My game is a simple rendition of the classic Hangman game, where the computer (Python) will randomly select one word out of a list of 10 words, and then prompt a player to guess the word in 7 tries or less. The player is able to guess one letter at a time, by typing that letter in either lowercase or uppercase characters. The letters of the chosen word are shown by a row of dashes representing each letter of the unknown word.  Every time a player guesses a letter incorrectly, a body part is drawn onto a drawing of a stick-figure being hung, bringing the player closer to losing. Conversely, if they guess a letter correctly, its position in the word is revealed and no body parts are added to the hangman. If the player is unable to guess the word correctly in 7 tries, all body parts of the hangman are drawn, and the player loses. However, if they guess the word in under 7 tries, the hangman is saved and the player wins. 

**Things to include in game:**

* `print()`
* `input()`
* At least one of:
  * `=`, `+=`, `-=`,`*=`, or`/=`
* at least one string
* at least one integer or a float
* At least one of:
  * `+`, `-`, `*`, or `/`
* At least one of:
  * `if`, `elif`, or `else` 
* At least one of:
  * `for` or `while`
* At least one of:
  * `==`, `!=`, `<`, `<=`, `>`, or `>=`
* At least one of:
  * `and`, `or`, or `not`

**Changes Made:** 

I added a hint system to my game to help players guess the hidden word more easily. After my changes, the program now asks the player if they would like a hint which reveals one of the letters in the word. If they do not want a hint, they can press any characters and the game will resume as normal. If they do choose to take a hint, one letter of the word will be revealed, but they will lose 2 out of their 7 tries at guessing the word. This is to make the game more challenging, as well as to ensure that no player uses just hints to guess every letter in the word. 

**Overall Reflection:**

Throughout this project, I really enjoyed the process of building a classic game that is both entertaining and challenging. Having never programmed a game in Python before, I was really excited to see my ideas come to fruition in the form of a functioning game. This project also enabled me to gain a deeper understanding and appreciation of the underlying mechanics behind some of the video games that we play today. 




