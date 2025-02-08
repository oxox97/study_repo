# 투 포인터 감 잡음
# 자기 제외한 두 수인 조건 망각
# 007.주몽과 같이 정렬한 리스트에서 끝에서 시작하여 작으면 s+=1, 크면 e-=1 하는 O(nlogn) * N 문제

import sys
input = sys.stdin.readline

N = int(input())
lst = sorted([int(i) for i in input().split()])

answer_list = []

for i, value in enumerate(lst):
    #print("\n> value :", value)
    s = 0
    e = N-1
    while s < e:
        if s == i:
            s += 1
        if e == i:
            e -= 1
        if s != e:
            current_sum = lst[s] + lst[e]
            #print(lst[s], '+', lst[e], '=', current_sum)
            if current_sum == value:
                answer_list.append([lst[s], lst[e], value])
                break
            elif current_sum > value:
                e -= 1
            else:
                s += 1

#print(answer_list)
print(len(answer_list))
