# 거의 소수 : 소수^n

import math

A, B = map(int, input().split())

is_prime = [True] * (int(math.sqrt(B)+1))  # 핵심 : sqrt(B)까지만 만들기 (메모리 절약)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(math.sqrt(B))+1):  # 사실 여기선 sqrt(sqrt(B))까지만 보면 됨
    if is_prime[i]:
        for j in range(i*i, int(math.sqrt(B)+1), i):
            is_prime[j] = False

answer_list = []
cnt = 0
for i in range(2, int(math.sqrt(B))+1):
    if is_prime[i]:
        top = 2
        #print("\n> i :", i)
        while i ** top <= B:
            #print(i ** top)
            answer_list.append(i ** top)
            top += 1
            cnt += 1

answer_list = [a for a in answer_list if A <= a]
print(len(answer_list))
#print(cnt)
#print(answer_list)