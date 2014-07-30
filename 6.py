#Sum square difference
#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#The answer is 25164150

n = 100
sumOfSquares = 0
squareOfSum = 0

# for i in range(1, n+1):
	# sumOfSquares += i*i
	# squareOfSum += i
	# print(i, sumOfSquares, squareOfSum)

# squareOfSum *= squareOfSum

sumOfSquares = int(n*(n+1)*(2*n+1)/6)
squareOfSum = int((1+n)*n*(1+n)*n/4)

print(squareOfSum, sumOfSquares, squareOfSum-sumOfSquares)
