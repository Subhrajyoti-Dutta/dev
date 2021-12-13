from fibonacci import fib, fib2

import time
n = 10000
a = time.time()
fib(n)
b = time.time()
fib2(n)
c = time.time()

print((b-a)/(c-b))