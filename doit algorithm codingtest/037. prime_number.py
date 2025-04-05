import math

M, N = map(int, input().split())
#M, N = 3, 16
lst = list(i for i in range(M, N+1))

#print(lst)

is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(N))+1, 1):  # 핵심 1) sqrt(N)까지 ⭐️
    # print("> i :", i)
    if is_prime[i]:
        for j in range(i*i, N+1, i):  # 핵심 2) i*i부터 체크 ⭐️
            is_prime[j] = False
            # print(j)

for i in range(M, N+1):
    if is_prime[i]:
        print(i)