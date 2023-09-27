'''
Margaret Harriman
06/23/2023
Program Assignment #2 - Playfair Cipher
CS 3626_W01
'''

import string
import math

## Initialize variables
alphabet = list(string.ascii_uppercase)  ## copy of the alphabet in all caps
matrix = []

## Keep track of how many slots are left to insert
## alphabet after key is inserted
matrixCounter = 0

## Keep track which two letters are combined in the matrix (I/J, Y/Z, etc.)
combinedIndex = 0

## Split user input plaintext into list of single characters
plaintextSplit = []

## Process plaintextSplit list into preprocessedList
preprocessedList  = []

## Decrypt preprocessedList back to original form
postprocessedList  = []

## For print formatting
stringifyMatrix = ""

'''
Some good words to use:
brick, feast, abduct, permit, phonic, joyance,
algorithm, breakdown, copyright, farmhouse
'''
## Get key from user, change all letters to
## uppercase for simplicity
playfairKey = input("Enter a word that has no repeating letters: ").upper()

## Add key to 5x5 matrix
for i in range(len(playfairKey)):
    matrix.append(playfairKey[i])
    matrixCounter += 1

## Now fill rest of matrix slots with remaining alphabet
for q in range(len(alphabet)):
    
    ## If the letter isn't already in the matrix, add it
    ## and keep track of where 'I' and 'J' are to combine
    if (alphabet[q] not in matrix):
        if (alphabet[q] == 'I' and 'J' not in matrix):
            matrix.append('I/J')
            combinedIndex = q
        elif (alphabet[q] == 'J' and 'I/J' in matrix):
            pass
        
        ## If both 'I' and 'J' are in the key, combine Y/Z
        elif (alphabet[q] == 'Y' and 'Z' not in matrix):
            matrix.append('Y/Z')
            combinedIndex = q
        elif (alphabet[q] == 'Z' and 'Y/Z' in matrix):
            pass
        else:
            matrix.append(alphabet[q])
            
        ## If I, J, Y, and Z aren't available to combine,
        ## just combine the final two letters in the matrix
        if (len(matrix) > 25):
            matrix[24] = matrix[24] + '/' + matrix[25]
            matrix.pop(-1)

## Create formatted matrix for pretty printing     
for k in range(len(matrix)):
    if (k % 5 == 0):
        stringifyMatrix += "\n"
    stringifyMatrix += ("%8s" % (matrix[k]))

print(stringifyMatrix)

## Get plaintext from user, change all letters to
## uppercase for simplicity, remove all spaces
plaintext = input("\nNow enter a plaintext to encode: ").upper().replace(" ", "")

## Split plaintext into list of single characters for easier manipulation
plaintextSplit = [*plaintext]

## Now break up the plaintext into pairs of letters
## and store the pairs in the preprocessedList object
for item in range(0, len(plaintextSplit), 2):
    
    ## Attach an 'X' at the end of the list if
    ## there's only one letter left
    if (item + 1 >= len(plaintextSplit)):
        preprocessedList.append(plaintextSplit[item] + 'X')
        
    ## If the two letters in the pair are identical,
    ## split them with an inserted 'X'
    elif (plaintextSplit[item] == plaintextSplit[item + 1]):
        preprocessedList.append(plaintextSplit[item] + 'X')
        plaintextSplit.insert(item + 1, 'X')
    else:
        preprocessedList.append(plaintextSplit[item] + plaintextSplit[item + 1])

print("Preprocessed List:", preprocessedList)

## Convert each pair of letters in preprocessedList to
## corresponding encrypted letters
def encrypt(keyMatrix, plaintextList):
    encryptedPlaintext = ""
    ## Grab the index that contains two letters
    ## and split them in two
    combinedIndex = [i for i in range(len(keyMatrix)) if len(keyMatrix[i]) > 1]
    combinedLetters = [keyMatrix[combinedIndex[0]][0], keyMatrix[combinedIndex[0]][-1]]
    firstCombinedIndex = keyMatrix[combinedIndex[0]][0]
    secondCombinedIndex = keyMatrix[combinedIndex[0]][-1]

    ## Helper function to determine which row an item is in
    def establishRowNumbers(index):
        if (index > 19):
            return 4
        if (index > 14):
            return 3
        if (index > 9):
            return 2
        if (index > 4):
            return 1
        return 0

    ## Helper function to determine which column an item is in
    def establishColNumbers(index):
        if (index % 5 == 0):
            return 0
        if (index % 5 == 1):
            return 1
        if (index % 5 == 2):
            return 2
        if (index % 5 == 3):
            return 3
        return 4

    ## 
    def assignNewRolCol(first, second):
        tempString = ""
        rows = [establishRowNumbers(first), establishRowNumbers(second)]
        cols = [establishColNumbers(first), establishColNumbers(second)]
        sameRow = (rows[0] == rows[1])
        sameCol = (cols[0] == cols[1])
        
        if (first == second):
            tempString = keyMatrix[first] + keyMatrix[second]
            return tempString
        if (sameRow):
            if ((first + 1) % 5 == 0):
                first -= 4
            else:
                first += 1
            if ((second + 1) % 5 == 0):
                second -= 4
            else:
                second += 1
            tempString = keyMatrix[first] + keyMatrix[second]
            return keyMatrix[first] + keyMatrix[second]
        if (sameCol):
            tempString = keyMatrix[(first + 5) % 25] + keyMatrix[(second + 5) % 25]
            return tempString
        tempString = keyMatrix[rows[0] * 5 + cols[1]] + keyMatrix[rows[1] * 5 + cols[0]]
        return tempString

    for pair in range(len(plaintextList)):
        first = 0
        second = 0

        if (plaintextList[pair][0] in combinedLetters):
            first = combinedIndex[0]
        else:
            first = keyMatrix.index(plaintextList[pair][0])
        if (plaintextList[pair][1] in combinedLetters):
            second = combinedIndex[0]
        else:
            second = keyMatrix.index(plaintextList[pair][1])
        encryptedPlaintext += assignNewRolCol(first, second)

    return encryptedPlaintext

def decrypt(keyMatrix, encryptedList):
    decryptedPlaintext = ""
    ## Grab the index that contains two letters
    ## and split them in two
    combinedIndex = [i for i in range(len(keyMatrix)) if len(keyMatrix[i]) > 1]
    combinedLetters = [keyMatrix[combinedIndex[0]][0], keyMatrix[combinedIndex[0]][-1]]
    firstCombinedIndex = keyMatrix[combinedIndex[0]][0]
    secondCombinedIndex = keyMatrix[combinedIndex[0]][-1]

    ## Helper function to determine which row an item is in
    def establishRowNumbers(index):
        if (index > 19):
            return 4
        if (index > 14):
            return 3
        if (index > 9):
            return 2
        if (index > 4):
            return 1
        return 0

    ## Helper function to determine which column an item is in
    def establishColNumbers(index):
        if (index % 5 == 0):
            return 0
        if (index % 5 == 1):
            return 1
        if (index % 5 == 2):
            return 2
        if (index % 5 == 3):
            return 3
        return 4

    ## 
    def assignNewRolCol(first, second):
        tempString = ""
        rows = [establishRowNumbers(first), establishRowNumbers(second)]
        cols = [establishColNumbers(first), establishColNumbers(second)]
        sameRow = (rows[0] == rows[1])
        sameCol = (cols[0] == cols[1])
        
        if (first == second):
            tempString = keyMatrix[first] + keyMatrix[second]
            return tempString
        if (sameRow):
            if ((first - 1) % 5 == 0):
                first += 4
            else:
                first -= 1
            if ((second - 1) % 5 == 0):
                second += 4
            else:
                second -= 1
            if (len(keyMatrix[first]) > 1):
                if (len(keyMatrix[second]) > 1):
                    tempString = keyMatrix[first][0] + keyMatrix[second][0]
                else:
                    tempString = keyMatrix[first][0] + keyMatrix[second]
            else:
                tempString = keyMatrix[first] + keyMatrix[second]
            return keyMatrix[first] + keyMatrix[second]
        if (sameCol):
            if (len(keyMatrix[(first - 5) % 25]) > 1):
                if (len(keyMatrix[(second - 5) % 25]) > 1):
                    tempString = keyMatrix[(first - 5) % 25][0] + keyMatrix[(second - 5) % 25][0]
                else:
                    tempString = keyMatrix[(first - 5) % 25][0] + keyMatrix[(second - 5) % 25]
            else:
                tempString = keyMatrix[(first - 5) % 25] + keyMatrix[(second - 5) % 25]
            return tempString
        if (len(keyMatrix[rows[0] * 5 + cols[1]]) > 1):
            if (len(keyMatrix[rows[1] * 5 + cols[0]]) > 1):
                tempString = keyMatrix[rows[0] * 5 + cols[1]][0] + keyMatrix[rows[1] * 5 + cols[0]][0]
            else:
                tempString = keyMatrix[rows[0] * 5 + cols[1]][0] + keyMatrix[rows[1] * 5 + cols[0]]
        else:
            tempString = keyMatrix[rows[0] * 5 + cols[1]] + keyMatrix[rows[1] * 5 + cols[0]]
        return tempString

    for pair in range(len(postprocessedList)):
        first = 0
        second = 0

        if (postprocessedList[pair][0] in combinedLetters):
            first = combinedIndex[0]
        else:
            first = keyMatrix.index(postprocessedList[pair][0])
        if (postprocessedList[pair][1] in combinedLetters):
            second = combinedIndex[0]
        else:
            second = keyMatrix.index(postprocessedList[pair][1])
        decryptedPlaintext += assignNewRolCol(first, second)
    return decryptedPlaintext

## Encrypt preprocessedList 
print(encrypt(matrix, preprocessedList))

## Put encrypted message into a list of letter pairs
postprocessedList = [encrypt(matrix, preprocessedList)[i:i + 2] for i in range(0, len(encrypt(matrix, preprocessedList)), 2)]
print (postprocessedList)
## Decrypt postprocessedList
print(decrypt(matrix, postprocessedList))






    
