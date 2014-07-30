#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#The answer is 6857

from math import sqrt

num = 600851475143

def isPrimeNaive(num):
    for i in range(2, num):
        if num%i == 0:
            return False;
    return True;

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
    
primeList = generatePrimeList(int(sqrt(num)))

for i in range(2, int(sqrt(num))):
    if isPrime(primeList, i) and num%i == 0:
        print("primeFactor", i)
