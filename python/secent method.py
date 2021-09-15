import math

def f(num): return 3*num - math.cos(num)-1

a = 0
b = 1

fa = round(f(a),3)
fb = round(f(b),3)

print(f"x0 = {a}")
print(f"f0 = {fa}\n")
print(f"x1 = {b}")
print(f"f1 = {fb}\n")

for i in range(2,10):
    c = round((a*fb - b*fa)/(fb-fa),3)
    print(f"x{i} = {c}")
    a, b = b, c
    fa, fb = fb, round(f(b),3)
    print(f"f{i} = {fb}\n")