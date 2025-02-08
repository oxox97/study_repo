import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

for j in range(1,N):  # range(N-1)
    for i in range(N-j):  # range(N-j-1)
        if lst[i] > lst[i+1]:
            # tmp = lst[i+1]
            # lst[i+1] = lst[i]
            # lst[i] = tmp
            lst[i+1], lst[i] = lst[i], lst[i+1]  # pythonic한 방식
        #print(lst)

for i in lst:
    print(i)
