# Author: Aditya Inapurapu
import math
import sys
import scipy
import redis
import requests

def main():
	r = redis.StrictRedis(host="0.0.0.0", port=6379)
	current_prime = str(r.get('current_prime'))
	i = 2
	if (int(current_prime) > 0):
		i = current_prime
	counter = 1
	while (i > 1):
		if (isPrime(int(i))):
			print(str(i))
			r.zadd('primes', counter, i)
			r.set('current_prime', i)
			postToDashing(i)
			counter = int(counter) + 1
		i = int(i) + 1
	r.close()

def postToDashing(prime):
	url = 'https://iaditya.herokuapp.com/widgets/prime'
	payload = '{ "auth_token": "YOUR_AUTH_TOKEN", "title": %s }' % (prime) 
	headers = '{content-type: application/json}'
	response = requests.post(url, data=payload)

def isPrime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

main()
