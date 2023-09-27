'''
Margaret Harriman
07/21/2023
Program Assignment #4 - RSA
CS 3626_W01
'''
from math import gcd
import random

## All prime numbers between 10 and 1000.
primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
          167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
          227, 229, 233, 239, 241, 251, 257, 263, 269, 271,
          277, 281, 283, 293, 307, 311, 313, 317, 331, 337,
          347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
          401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
          461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
          523, 541, 547, 557, 563, 569, 571, 577, 587, 593,
          599, 601, 607, 613, 617, 619, 631, 641, 643, 647,
          653, 659, 661, 673, 677, 683, 691, 701, 709, 719,
          727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
          859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
          937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

## Choose two prime numbers from the above list at random
## and store them in variables p and q.
# Also grab their indices.
p = primes[random.randint(0, len(primes))]
pIndex = primes.index(p)
q = primes[random.randint(0, len(primes))]
qIndex = primes.index(q)

## Extended Euclidean Algorithm
def extEuclidAlgo(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extEuclidAlgo(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

## Key generator function that takes p and q as parameters
## and creates a Public Key and Private Key
def keyGenerator(p, q):
    publicKey =[]
    privateKey =[]
    
    n = p * q
    phiOfN = (p - 1) * (q - 1)
    e = 7
    d = extEuclidAlgo(e, phiOfN)[1]

    publicKey = [e, n]
    privateKey = [d, n]

    return publicKey, privateKey

## The main RSA algorithm, which takes a plaintext and key
## and returns the ciphertext
def rsaAlgo(plaintext, key):
    textToAlter = int(plaintext)

    return (textToAlter ** key[0]) % key[1]

## The same RSA algorithm as above but encrypts
## a string instead of one number
def rsaAlgoMultiRounds(plaintext, key):
    asciiList = [ord(elem) for elem in [*plaintext]]
    print("ASCII list before:", asciiList)
    changedText = []
    for i in range(len(plaintext)):
        changedText.append(rsaAlgo(asciiList[i], key))
    return changedText

## Print two rounds of code: the first round
## uses the prime numbers from our textbook, 17 and 11
input("This first round will use prime numbers 17 and 11 from our textbook. Press Enter to continue...")
print ("\nP and Q: 17 and 11")
print("\nPublic key:", keyGenerator(17,11)[0], "\nPrivate key:", keyGenerator(17,11)[1])
userInput = input("\nEnter a plaintext to be encrypted: ").lower()
print ("ASCII list after: ", rsaAlgoMultiRounds(userInput, keyGenerator(17,11)[0]))

## The second round depends on picking two prime numbers at random
## from the list above
input("\n\nThis round will use two random prime numbers. Press Enter to continue...")
print ("P and Q:", p, q)
print("\nPublic key:", keyGenerator(primes[pIndex], primes[qIndex])[0], "\nPrivate key:", keyGenerator(primes[pIndex], primes[qIndex])[1])
userInput = input("\nEnter a plaintext to be encrypted: ").lower()
print ("ASCII list after: ", rsaAlgoMultiRounds(userInput, keyGenerator(primes[pIndex], primes[qIndex])[0]))




