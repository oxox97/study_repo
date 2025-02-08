from collections import deque

N = int(input())

dq = deque([i+1 for i in range(N)])

while len(dq)>1:
    #print(dq)
    dq.popleft()
    #print(dq)
    dq.append(dq[0])  # dq.append(dq.popleft()) 한 번에
    #print(dq)
    dq.popleft()
    #print(dq)

print(dq[0])
print(dir(dq))