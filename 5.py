#Smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#The answer is 232792560

from fractions import gcd

def lcm(a, b):
	return int(a*b/gcd(a,b))

j = 1
for i in range(2, 20):
	j = lcm(i, j)

print(j)
