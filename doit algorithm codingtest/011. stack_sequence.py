import sys
input = sys.stdin.readline

N = int(input())
lst = [int(i) for i in range(1, N+1)]
answer = [int(input()) for i in range(N)]

answer_list = []
stk = []

idx = 0

for i in lst:
    stk.append(i)
    answer_list.append(["+", i])

    while stk and answer[idx] == stk[-1]:
        stk.pop(-1)
        answer_list.append(["-", i])
        idx += 1

if stk:
    print("NO")
else:        
    for a in answer_list:
        print(a[0])