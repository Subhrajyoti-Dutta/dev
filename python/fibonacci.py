import sys
sys.setrecursionlimit(2**31-1)

def fib(n, fibTable = dict()):
	if n == 0 or n == 1: 
		return n
	elif n in fibTable:
		return fibTable[n]
	else: 
		val = fib(n-1, fibTable) + fib(n-2, fibTable)
		fibTable[n] = val
		return val

def fib2(n):
	a = 0
	b = 1

	for i in range(n-1):
		a, b = b, a+b

	return b

if __name__ == "__main__":
	import time
	a = time.time()
	print(fib(1000))
	b = time.time()
	print(b-a)