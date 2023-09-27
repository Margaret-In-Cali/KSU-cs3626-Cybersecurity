'''
Margaret Harriman
06/11/2023
Program Assignment #1
CS 3626_W01
'''

## function to take user's input and convert to list, ASCII, and Binary
def fromStringTo(userInput):
    ## This is the string that will be returned
    finalString = ""
    
    ## convert to list by unpacking user input, concatenate to finalString
    finalString += "To a List: " + str([*userInput])

    ## convert to ASCII by converting each individual
    ## character in the unpacked list, concatenate to finalString
    convertedString = [ord(elem) for elem in [*userInput]]
    finalString += "\nTo ASCII: " + str(convertedString)

    ## convert to binary by converting each individual
    ## element of the unpacked list, concatenate to finalString
    finalString += "\nTo binary: " + str([format(int(elem), 'b') for elem in convertedString])
    
    return finalString

def fromListTo(userInput):
    ## This is the string that will be returned
    finalString = ""
        
    ## Concatenate only odd numbered indices to
    ## remove unnecessary spaces from userInput
    finalString += "To String: " + userInput[::2]

    ## convert to ASCII by converting each individual
    ## character in the unpacked list, concatenate to finalString
    convertedString = [ord(elem) for elem in [*userInput[::2]]]
    finalString += "\nTo ASCII: " + str(convertedString)

    ## convert to binary by converting each individual
    ## element of the unpacked list, concatenate to finalString
    finalString += "\nTo binary: " + str([format(int(elem), 'b') for elem in convertedString])
    
    return finalString    

## function to take user's input and convert to string, list, and binary
def fromASCIITo(userInput):
    ## This is the string that will be returned
    finalString = ""

    ## convert userInput into list and then convert each string ASCII character
    ## into actual ASCII character
    convertedASCII = [ord(elem) for elem in [*userInput]]
    ## Then join those ASCII characters into one string, concatenate to finalString
    convertedASCII = ''.join([chr(int(elem)) for elem in userInput.split(" ")])
    finalString += "To String: " + str(convertedASCII)

    ## convert newly created string into list by unpacking, concatenate
    finalString += "\nTo List: " + str([*convertedASCII])

    ## convert each item in unpacked list to binary, concatenate
    convertedString = [ord(elem) for elem in [*convertedASCII]]
    finalString += "\nTo binary: " + str([format(int(elem), 'b') for elem in convertedString])
    
    return finalString

## function to take user's input and convert to string, list, and ASCII
def fromBinaryTo(userInput):
    ## This is the string that will be returned
    finalString = "To String: "
    tempString = ""

    #convert userInput into list of string Binary numbers
    convertedBinary = userInput.split(" ")

    ## convert each item in our list into English, capturing
    ## each item in two lists
    for binaryItem in convertedBinary:
        finalString += chr(int(binaryItem, 2))
        tempString += chr(int(binaryItem, 2))

    ## Unpack the converted userInput into a list, concatenate
    finalString += "\nTo List: " + str([*tempString])

    ## Convert list into ASCII, concatenate
    finalString += "\nTo ASCII: " + str([ord(elem) for elem in [*tempString]])
    
    return finalString    

print(fromStringTo(input('Enter first and last name as string: ')))
print()
print(fromListTo(input('Enter first and last name as list of characters, each separated by a space: ')))
print()
print(fromASCIITo(input('Enter first and last name as ASCII codes: ')))
print()
print(fromBinaryTo(input('Enter first and last name as Binary numbers: ')))
print()
print()
print(fromStringTo(input('Enter a sentence as string: ')))
print()
print(fromListTo(input('Enter a sentence as list of characters, each separated by a space: ')))
print()
print(fromASCIITo(input('Enter a sentence as ASCII codes: ')))
print()
print(fromBinaryTo(input('Enter a sentence as Binary numbers: ')))


