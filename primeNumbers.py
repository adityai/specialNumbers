# Author: Aditya Inapurapu
import math
import sys
import scipy
import redis
import requests
import os

def main():
	r = redis.StrictRedis(host="primeredis", port=6379)
	# r = redis.StrictRedis(host="0.0.0.0", port=6379)
	current_prime = r.get('current_prime')
	i = 2
	if (not current_prime):
		current_prime = "2"
	if (int(current_prime) > 0):
		i = current_prime
	counter = 1
	print(current_prime)
	while (i > 1):
		if (isPrime(int(i))):
			print(i)
			r.zadd('primes', { int(counter): int(i)} )
			r.set('current_prime', i)
			postToDashing(i)
			counter = int(counter) + 1
		i = int(i) + 1
	r.close()

def postToDashing(prime):
	token = os.environ.get('AUTH_TOKEN')
	url = os.environ.get('DASHING_URL')
	payload = '{ "auth_token": "%s" , "title": %s }' % (token, prime) 
	headers = '{content-type: application/json}'
	response = requests.post(url, data=payload)
	print(response)

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
