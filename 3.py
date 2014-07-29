#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def getPrimeList(maxNum):
    res = [True]*maxNum
    res[0] = False
    res[1] = False
    for i in range(2, maxNum):
        for j in range(i+i, maxNum, i):
            res[j] = False
    return res

def isPrime(primeList, num):
    return primeList[num]

def primeFactors(num):
    primeList = getPrimeList(int(sqrt(num/2)))
    for i in range(2, num):
        if num%i == 0 and isPrime(primeList, i):
            print(i)
            print(int(num/i))

primeFactors(600851475143)
