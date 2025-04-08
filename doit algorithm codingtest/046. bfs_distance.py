from collections import deque
import sys
input = sys.stdin.readline  # 시간 초과 방지 

N, M, K, X = map(int, input().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

for j in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

# print(graph)

def bfs_distance(graph, X):

    # define
    queue = deque()
    distance = [-1] * (N+1)

    # start
    queue.append(X)
    distance[X] = 0

    # loop
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[curr] + 1

    return distance

answer = bfs_distance(graph, X)
result = [i for i, d in enumerate(answer) if d == K]
if result:
    for x in result:
        print(x)
else:
    print(-1)