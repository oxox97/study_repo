# 투 포인터
# 양 끝단에서 시작 + 자기 자신 제외
# O(nlogn) * N 문제

import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))

a_list = []
for i, v in enumerate(lst):
    s, e = 0, len(lst)-1
    while s < e:
        if s == i:
            s += 1
        elif e == i:
            e -= 1
        else:
            curr_sum = lst[s] + lst[e]
            # print(v, curr_sum)
            if curr_sum == v:
                a_list.append(v)
                break
            elif curr_sum < v:
                s += 1
            else:
                e -= 1

print(len(a_list))