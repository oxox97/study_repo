# import sys
# input = sys.stdin.readline

# N = int(input())
# lst = [int(input()) for _ in range(N)]

# for j in range(1,N):  # range(N-1)
#     for i in range(N-j):  # range(N-j-1)
#         if lst[i] > lst[i+1]:
#             # tmp = lst[i+1]
#             # lst[i+1] = lst[i]
#             # lst[i] = tmp
#             lst[i+1], lst[i] = lst[i], lst[i+1]  # pythonic한 방식
#         #print(lst)

# for i in lst:
#     print(i)


import heapq
import sys

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for i in range(N)]

#lst = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]

hq = []
for i in lst:
    if i==0:
        if not hq:
            print(0)
        else:
            #print(hq)
            a = heapq.heappop(hq)
            print(a[1])
            
    else:
        heapq.heappush(hq, (abs(i), i))
        #print(hq)
        
#print(hq)

# heapq.heappush(heap, item)
# heapq.heappop(heap)
# heap.heapify(iterable) : 리스트 최소 힙으로 제자리 변환 (return None)
# heap.nsmallest(n, iterable)