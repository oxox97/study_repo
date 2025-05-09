# 투포인터
# sorted 양 끝단에서 줄이기
# 합이 기준보다 크면, e -= 1 / 작으면, s += 1

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = sorted([int(i) for i in input().split()])

# print(lst)

s = 0
e = len(lst)-1
cnt = 0

while s < e:
    curr_sum = lst[s] + lst[e]
    if curr_sum == M:
        cnt += 1
        s += 1
        e -= 1
    elif curr_sum > M:
        e -= 1
    else:
        s += 1

print(cnt)