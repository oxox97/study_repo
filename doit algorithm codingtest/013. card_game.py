import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

lst = deque([int(i) for i in range(1,N+1)])

while len(lst) > 1:
    lst.popleft()
    lst.append(lst.popleft())

print(lst[0])