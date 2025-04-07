import math

A, B = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(str(1) * gcd(A, B))