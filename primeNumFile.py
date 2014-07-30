#Generate prime numbers binary file

from math import sqrt

maxNumber = 9999999

def isPrime(primeList, num):
    try:
        return primeList[num]
    except IndexError:
        return False

def generatePrimeList(max):
    primeList = [True]*max
    upper = int(sqrt(max))
    for i in range(2, upper):
        if primeList[i]:
            for j in range(i+i, max, i):
                primeList[j] = False
    return primeList

primeList = generatePrimeList(maxNumber)
binaryPrimeList = bytearray(primeList)

#open file
fout = open("prime", "wb")
fout.write(binaryPrimeList)
