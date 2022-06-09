import random, sys

def miller_rabin_pass(a, s, d, n):

	a_to_power = pow(a, d, n)
	i=0

	if a_to_power == 1:
		return True
	

	while(i < s-1):
		if a_to_power == n - 1:
			return True
		a_to_power = (a_to_power * a_to_power) % n
		i+=1

	return a_to_power == n - 1

def miller_rabin(n):

	s = 0
	while d%2 == 0:
		d >>= 1
		s+=1
	

	K = 20
	
	i=1
	while(i<=K):
	# 1 < a < n-1
		a = random.randrange(2,n-1)
		if not miller_rabin_pass(a, s, d, n):
			return False
		i += 1

	return True

def gen_prime(nbits):

	while True:
			p = random.getrandbits(nbits)

			p |= 2**nbits | 1
			if miller_rabin(p):
				return p
				break

def gen_prime_range(start, stop):

	while True:
		p = random.randrange(start,stop-1)
		p |= 1
		if miller_rabin(p):
				return p
				break

if __name__ == "__main__":
	if sys.argv[1] == "test":
		n = sys.argv[2]
		print(miller_rabin(n) and "PRIME" or "COMPOSITE")
	elif sys.argv[1] == "genprime":
		nbits = int(sys.argv[2])
		print(gen_prime(nbits))

		
