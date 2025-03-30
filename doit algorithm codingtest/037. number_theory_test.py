from datetime import datetime

M, N = map(int, input().split())
lst = list(i for i in range(M, N+1))

print(lst)

for i in lst:
    # sqrt(N)까지만 보면 됨