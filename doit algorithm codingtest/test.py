# 구간 합 알고리즘 ⭐️
# O(N+M)
# 1. 정의 : prefix_sum = [0] * (N+1)  # base는 합의 항등원인 0 (곱은 1)
# 2. prefix_sum[i+1] = prefix_sum[i] + lst[i]
# 3. a = prefix_sum[e] - prefix_sum[s-1]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

prefix_sum = [0] * (N+1)  # base는 합의 항등원인 0 (곱은 1)

for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + lst[i]

for _ in range(M):
    s, e = map(int, input().split())
    a = prefix_sum[e] - prefix_sum[s-1]
    print(a)