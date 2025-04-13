# 일단 패스...?
# 답은 맞는 것 같은데 시간 초과고, DFS로 풀어야 할 것 같음 (아닌가)

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

graph = {}
for i in range(1, N+1):
    graph[i] = []

for i in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)  # 반대

def bfs_distance(graph, start_node):
    # define
    queue = deque()
    distance = [-1] * (N+1)

    # start
    queue.append(start_node)
    distance[start_node] += 1

    # loop
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if distance[next] == -1:
                queue.append(next)
                distance[next] = distance[curr] + 1
    
    return start_node, max(distance)

answer_dict = {}
for i in range(1, N+1):
    start_node, max_distance = bfs_distance(graph, i)
    answer_dict[start_node] = max_distance

# print(answer_dict)

answer = [k for k,v in answer_dict.items() if v == max(answer_dict.values())]
for a in answer:
    print(a, end=" ")