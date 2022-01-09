import time

def add():
	x = 0
	for i in range(10000000+1):
		x += i
	print(x)

a = time.time()
add()
b = time.time()

print(b-a)