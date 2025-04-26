# 나머지 합 구하기
# ⭐️ 나머지가 같은 누적합 인덱스 쌍의 수를 조합으로 구하는 문제
# 알고리즘 : if S[i] % M == S[j] % M -> (S[i] - S[j]) % M == 0
# 순열로 경우의 수 계산

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 나머지 구해서 누적합 만들기
psum = [0] * (N + 1)
for i in range(N):
    psum[i + 1] = psum[i] + lst[i]

psum_remainder = [i % M for i in psum]

remainder_count = [0] * M
for i in psum_remainder:
    remainder_count[i] += 1

# 조합 계산 : nC2 = n(n-1)/2
cnt = 0
for i in remainder_count:
    a = int(i * (i-1) / 2)
    cnt += a
print(cnt)