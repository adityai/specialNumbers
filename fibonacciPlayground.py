# Author: Aditya Inapurapu
import math
import sys
import scipy

def main():
	if len(sys.argv) <= 1:
		i = 1
		print("Searching for perfect fibonacci numbers:")
		while i > 0:
			if (isFibonacci(i)):
				print(i)
				f = open("fibonacci.txt", "a+")
				f.write(str(i) + "\n")
				if (isPerfect(i)):
					print("Perfect Fibonacci:" + i)
					f.write("Perfect Fibonacci:" + str(i) + "\n")
				f.close()
			i = i + 1
	else:
		if (isPrime(int(sys.argv[1]))):
			print(sys.argv[1] + " is Prime")
			if (isMersennePrime(int(sys.argv[1]))):
				print(sys.argv[1] + " is Mersenne Prime")
				
		if (isPerfect(int(sys.argv[1]))):
			print(sys.argv[1] + " is Perfect")
			
		if (isNarcissistic(sys.argv[1])):
			print(sys.argv[1] + " is Narcissistic")

		goldenNumberBefore = str(findGoldenBefore(int(sys.argv[1])))
		goldenNumberAfter = str(findGoldenAfter(int(sys.argv[1])))
		print("Golden ratio " +  goldenNumberBefore + " : " + sys.argv[1] + " : " + goldenNumberAfter)
		if (float(goldenNumberBefore).is_integer()):
			print("Nearly whole golden ratio " + goldenNumberBefore + " : " + sys.argv[1])
		if (float(goldenNumberBefore).is_integer()):
			print("Nearly whole golden ratio " + sys.argv[1] + " : " + goldenNumberAfter)

		if (isPerfectSquare(int(sys.argv[1]))):
			print(sys.argv[1] + " is a perfect square")

		if isFibonacci(int(sys.argv[1])):
			print(sys.argv[1] + " is a number in the Fibonacci sequence")

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def isPerfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def isMersennePrime(n):
	i = 1
	result = False
	while i > 0:
		if ((2**i) - 1 == n):
			print("Based on (2^" + str(i) + ")-1")
			result = True
			break
		i = i + 1
	return result

def isNarcissistic(n):
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

def isPerfectSquare(n):
	return float(n**0.5).is_integer();

def isFibonacci(n):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n == 0 or abs(round(a) - a) < 1.0 / n

main()
