'''
Margaret Harriman
07/07/2023
Program Assignment #3 - Feistel Cipher
CS 3626_W01
'''
import pprint

## Get a plaintext and key from user
userInput = input("Enter a plaintext to be encrypted: ").lower()
feistelKey = input("Now enter 4-letter key to be used in encryption: ").lower()

print ("\nPlaintext: ", userInput)
print ("Master key: ", feistelKey)

def feistelCipher(inputText, inputKey):
    
    '''
    These next two variables will become more
    useful when this code is made more robust
    to take on more rounds per execution
    '''
    
    ## Keep track of subkeys for decryption
    keysDict = {}

    ## Keep track of current round
    currentRound = 0
    
    keysDict[0] = inputKey
    currentRound += 1

    ## Helper function to create subkeys and track them
    def createSubKey(key):       
        subKey = [*key]
        
        ## Subkeys are created by moving the 0th index to the end
        ## of the subkey, i.e., 'abcdef' becomes 'bcdefa' after
        ## one iteration
        
        poppedIndex = subKey.pop(0)
        keysDict[currentRound] = (''.join(subKey) + poppedIndex)

        return (''.join(subKey) + poppedIndex)

    ## Create a new subkey for this round
    newSubKey = createSubKey(inputKey)
    print("This round's subkey: ", newSubKey)
    
    ## Break user input into lefthand and righthand chunks
    leftHand = userInput[0:int(len(userInput)/2)]
    rightHand = userInput[int(len(userInput)/2):]

    print("\nLefthand (L sub 0): ", leftHand)
    print("Righthand (R sub 0): ", rightHand)

    ## Convert items to binary to prepare to XOR
    leftHandBinary = ' '.join(format(ord(character), 'b') for character in leftHand).split(" ")
    rightHandBinary = ' '.join(format(ord(character), 'b') for character in rightHand).split(" ")
    subKeyBinary = ' '.join(format(ord(character), 'b') for character in newSubKey).split(" ")

    print ("L sub 0 in binary: ")
    pprint.pprint(leftHandBinary)
    print ("R sub 0 in binary: ")
    pprint.pprint(rightHandBinary)
    print ("Subkey in binary: ")
    pprint.pprint(subKeyBinary)
    print()

    ## Round function XORs R sub 0 with
    ## the subkey
    def roundFunction(textBlock, subKey):
        functionResult = ""
        for item in range(len(textBlock)):
            functionResult += ('{0:0{1}b}'.format(int(textBlock[item], 2) ^ int(subKey[item % len(subKey)], 2),
                                                  len(textBlock[item])) + ' ')
        return functionResult.split(" ")[0:-1]

    ## Store round function value
    funcOutcome = roundFunction(rightHandBinary, subKeyBinary)
    print("Function Output", funcOutcome)

    def finalXOR(funcResult, lefthand):
        xorString = ""
        for item in range(len(funcResult)):
            xorString += ('{0:0{1}b}'.format(int(funcResult[item], 2) ^ int(lefthand[item % len(lefthand)], 2),
                                                len(funcResult[item])) + ' ')
        return xorString.split(" ")[0:-1]

    ## Assign new lefthand (L sub 1) old righthand (R sub 0) value
    newLeftHand = rightHandBinary
    ## Store R sub 1 value
    newRightHand = finalXOR(funcOutcome, leftHandBinary)

    ##Print R sub 1 and L sub 1
    print ("\nR sub 1: ")
    pprint.pprint(newRightHand)
    print ("L sub 1: ")
    pprint.pprint(newLeftHand)


feistelCipher(userInput, feistelKey)
