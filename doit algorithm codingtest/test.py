import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

stk = []
candidates = [i for i in range(1, n+1)]
answer = []

idx = 0

while stk or candidates:
    if stk and stk[-1] == lst[idx]:
        answer.append("-")
        stk.pop()
        idx += 1
    elif candidates:
        answer.append("+")
        stk.append(candidates[0])
        candidates.pop(0)
    else:
        print("NO")
        sys.exit(0)

for a in answer:
    print(a)