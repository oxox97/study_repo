import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

changed = False

for i in range(N-1):
    changed = False
    #print(A)
    for j in range(N-i-1):
        if A[j] > A[j+1]:
            changed = True
            tmp = A[j]
            A[j] = A[j+1]
            A[j+1] = tmp
    if changed == False:
        print(i+1)
        break


