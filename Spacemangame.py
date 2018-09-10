from random import random,randint

wordsList = ["apple", "orange", "banana", "pineapple", "papaya", "tangerine", "kiwi", "cantelope", "watermelon", "honeydew", "grapefruit", "grape", "blueberry", "strawberry", "blackberry", "peach", "apricot", "cherry", "guava", "lemon", "lime", "mango", "lychee", "pear", "pomegranate" ]
guessesList = []
chosenWord = wordsList[randint(0,len(wordsList)-1)]
splitString = list(chosenWord) #splits string from wordsList into an array of its characters
userInputString = ["_"]*len(splitString)

def getUserGuesses():
    return input("This is a fruit. Guess a letter! ")

def displaySlashesEtc(placement):
    printString = ""
    for x in placement:
        printString += x
        printString += " "
    print (printString)
    print ("guessed letters: " + ', '.join(guessesList)) #prints without the brackets!

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
userNumWrongGuesses = 0
while(not("_" not in userInputString or userNumWrongGuesses>=7)):
    userInputString,userRight = replaceBlanks(splitString, userInputString)
    if not userRight:
        userNumWrongGuesses+=1
        print("WRONG!")
    displaySlashesEtc(userInputString)
if(userNumWrongGuesses>=7):
    print("You lose! The word was " + chosenWord)
else:
    print("YOU WIN!")
