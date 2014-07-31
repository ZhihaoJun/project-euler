#Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#The answer is 142913828922

def isPrime(primeList, num):
	if primeList[num]=="\001":
		return True
	return False

fin = open("prime")
primeList = fin.read()

sum = 0

for i in range(1, 2000000):
	if isPrime(primeList, i):
		sum += i

print(sum)
