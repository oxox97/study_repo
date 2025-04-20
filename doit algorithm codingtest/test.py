# 오큰수 (NGE)

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

answer = [-1] * (N)
stk = []  # ⭐️ 오큰수가 정해지지 않은 리스트의 인덱스 저장

for i in range(N):
    # 오큰수가 정해지지 않은 인덱스가 있고 (len(stk) > 0) &
    # 현재 기준 값이 스택 top 인덱스의 값보다 크면 (lst[i] > lst[stk[-1]])
    # 스택에서 해당 인덱스 제거(pop)하면서 오큰수 할당
    while stk and lst[i] > lst[stk[-1]]:
        answer[stk.pop()] = lst[i]   
    stk.append(i)  # 차례대로 인덱스 넣어주기

for a in answer:
    print(a, end=" ")