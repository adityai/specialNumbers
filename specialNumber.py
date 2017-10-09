# Author: Aditya Inapurapu
import math
import sys
import scipy

def main():
	if len(sys.argv) < 1:
		print("Enter the number you'd like to check")
	else:
		if (isPrime(int(sys.argv[1]))):
			print(sys.argv[1] + " is Prime")
			if (isMersennePrime(int(sys.argv[1]))):
				print(sys.argv[1] + " is Mersenne Prime")
		if (isPerfectNumber(int(sys.argv[1]))):
			print(sys.argv[1] + " is Perfect")
		if (isNarcissisticNumber(sys.argv[1])):
			print(sys.argv[1] + " is Narcissistic")

		goldenNumberBefore = str(findGoldenBefore(int(sys.argv[1])))
		goldenNumberAfter = str(findGoldenAfter(int(sys.argv[1])))
		print("Golden ratio " +  goldenNumberBefore + " : " + sys.argv[1] + " : " + goldenNumberAfter)
		if (float(goldenNumberBefore).is_integer()):
			print("Nearly whole golden ratio " + goldenNumberBefore + " : " + sys.argv[1])
		if (float(goldenNumberBefore).is_integer()):
			print("Nearly whole golden ratio " + sys.argv[1] + " : " + goldenNumberAfter)


def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def isPerfectNumber(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def isMersennePrime(n):
	i = 1
	while i > 0:
		if (2^i - 1 == n):
			return True
		i = i + 1

def isNarcissisticNumber(n):
	length = len(n) 
	intN = int(n)
	evalN = 0
	for i in range(0, length):
		evalN = evalN + (int(n[i])**length)
	if evalN == intN:
		return True

def findGoldenAfter(n):
	return float(n) * 1.618

def findGoldenBefore(n):
	return float(n) / 1.618

main()
