#amicable numbers under 10000 from project euler
#
#You need to take each pair of numbers under 10,000, obtain the list 
#of factors of each
#(note, not prime factors, just factors), sum the factors of each, 
#then compare them for  the “amicable” property.

#You will need a function:
#GetAllFactors(n) returning a list of all factors of n that are < n
#SumFactors(l) where l is a list of factors and the value returned is their sum
#AmicableCheck(a, b) which does the check

def GetAllFactors(n):
	if(n < 1):
		print("invalid input to GetAllFactors")
		return []

	factorList = []
	for i in range (1, n-1):
		if n % i == 0:
			factorList.append(i)

	return factorList

def SumFactors(l):
	curSum = 0
	for i in range(0, len(l)):
		curSum += l[i]
	return curSum

def AmicableCheck(a, b):
	if a == b:
		return False

	aFactors = GetAllFactors(a)
	bFactors = GetAllFactors(b)

	if aFactors != [] and bFactors != [] :
		aSum = SumFactors(aFactors)
		bSum = SumFactors(bFactors)

		if aSum == b and bSum == a:
			return True

	return False

for i in range(1, 10001):
	for j in range(1, 10001):
		if(AmicableCheck(i, j)):
			print(" amicable ", i, " ", j)

print("done")

