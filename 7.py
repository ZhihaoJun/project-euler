#10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#The answer is 104743

fin = open("prime", "rb")

primeList = fin.read()

primeNum = 0

for i in range(2, len(primeList)):
	if primeList[i] and primeNum<10001:
		primeNum += 1
		print(primeNum, i)
