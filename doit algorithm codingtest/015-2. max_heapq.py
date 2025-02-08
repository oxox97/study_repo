import heapq
import sys
input = sys.stdin.readline
lst = [5,1,2,3,7]

hq = [(-i, i) for i in lst]  # 음수 변환
heapq.heapify(hq)  # 최대 힙 변환 (O(N))

answer = [heapq.heappop(hq)[1] for _ in range(len(hq))]
print(answer)

# heapfiy() : O(N)
# heappush(), heappop() : O(log N)
# heap[0] : O(1)
# nsmallest() : O(N log N)