from random import random,randint

wordsList = ["apple", "orange", "banana", "pineapple", "papaya", "tangerine", "kiwi", "cantelope", "watermelon", "honeydew", "grapefruit", "grape", "blueberry", "strawberry", "blackberry", "peach", "apricot", "cherry", "guava", "lemon", "lime", "mango", "lychee", "pear", "pomegranate" ]
guessesList = []
# guessesList = [item.lower() for item in guessesList] #WHAT
chosenWord = wordsList[randint(0,len(wordsList)-1)]
splitString = list(chosenWord) #splits string from wordsList into an array of its characters
userInputString = ["_"]*len(splitString)
userNumWrongGuesses = 0
userGuessesRemaining = 7

def getUserGuesses():
    permittedStuff = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    while True:
        while True:
            try:
                letterGetter = input("This is a fruit. Guess a letter! ").lower()
                break
            except EOFError:
                print("ERROR. ENTER A LETTER")
        if (len(letterGetter) == 1 and letterGetter in permittedStuff):
            return letterGetter #I know it's an extra step - it was a thing I think I needed to do because of the .lower()
        print("ERROR. ENTER A LETTER")

def displaySlashesEtc(placement):
    printString = ""
    for x in placement:
        printString += x
        printString += " "
    print (printString)
    print ("guessed letters: " + ', '.join(guessesList)) #prints without the brackets!
    print ("You have " + str(userGuessesRemaining) + " guesses left!")

def replaceBlanks(split,uIn): #Here I'm trying to replace _ with correct guesses
    userGuess = getUserGuesses()
    guessesList.append(userGuess)
    altered = False
    for x in range(len(split)):
        if userGuess == split[x]:
            uIn[x] = splitString[x]
            altered = True
    return(uIn,altered)

displaySlashesEtc(userInputString)
userRight = True
while(not("_" not in userInputString or userNumWrongGuesses>=7)):
    userInputString,userRight = replaceBlanks(splitString, userInputString)
    if not userRight:
        userNumWrongGuesses+=1
        userGuessesRemaining = 7 - userNumWrongGuesses
        print("WRONG!")
    displaySlashesEtc(userInputString)
if(userNumWrongGuesses>=7):
    print("You lose! The word was " + chosenWord)
else:
    print("YOU WIN!")
