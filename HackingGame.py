import sys
import random

#Open dictionary
dictionary = open("enable1.txt", "r")

#Calculate number of words in dictionary
numLines = sum(1 for line in dictionary)

#Ask user for difficulty
print "Difficulty (1 - 5)?"

#Ensure difficulty is in range
inputReceived = 0
while inputReceived == 0:
    difficulty = sys.stdin.readline()
    difficulty = int(difficulty)
    if 1 <= difficulty <= 5:
        inputReceived = 1
    else:
        print "Please choose a valid difficulty in range 1 to 5"

#Determine word length for game
wordLength = 0

if difficulty == 1:
    wordLength = random.randint(4, 7)
elif difficulty == 2:
    wordLength = random.randint(7, 10)
elif difficulty == 3:
    wordLength = random.randint(10, 12)
elif difficulty == 4:
    wordLength = random.randint(12, 14)
elif difficulty == 5:   
    wordLength = random.randint(14, 16)
    
#Calculate number of words in this round of the game
wordCount = (3 * difficulty) + random.randint(1, 5)

wordList = []

#Generate random words
for i in range(wordCount):
    #generate target to get random next word
    nextTarget = random.randint(1, numLines)
    
    #Reset the dictionary to the start
    dictionary.seek(0)
    
    counter = 0
    
    #Go to the random point, then find next word with proper length
    for j in range(nextTarget):
        dictionary.readline()
        counter = counter + 1
    
    foundWord = 0
    
    while foundWord == 0:
        if counter == numLines:
            dictionary.seek(0)
            counter = 0
        
        temp = dictionary.readline()
        temp = temp.replace("\n", "")
        temp = temp.replace("\r", "")        
        if len(temp) == wordLength:
            foundWord = 1
            wordList.append(temp)
            print temp
        
        counter = counter + 1
        
#Determine which word the password is
passwordIndex = random.randint(0, wordCount)
password = wordList[passwordIndex]

guessesLeft = 4
passwordFound = 0

#While the player has guesses left, prompt them to guess the next word
while guessesLeft > 0:
    print "Guess(" + str(guessesLeft) + "/4)?"
    guess = sys.stdin.readline()
    guess = guess.replace("\n", "")
    #Check if the user guessed right
    if wordList.index(guess) == passwordIndex:
        passwordFound = 1
        guessesLeft = 0
    else:
        #Decrement number of guesses
        guessesLeft = guessesLeft - 1
        #Tell user how many they got right
        numberCorrect = 0
        for j in range(wordLength):
            if password[j] == guess[j]:
                numberCorrect += 1
        print str(numberCorrect) + "/" + str(wordLength) + " correct"

if passwordFound == 1:
    print "Congratulations! You win."
else:
    print "You lose. The correct password was: " + password