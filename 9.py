#Special Pythagorean triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#The answer is 200*375*425=31875000

for a in range(1, 998):
	for b in range(1, 1000-a):
		c = 1000-a-b
		if a*a+b*b==c*c:
			print(a, b, c, a*b*c)
