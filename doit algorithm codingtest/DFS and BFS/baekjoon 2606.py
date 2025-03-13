from collections import deque

N = int(input())
num_edge = int(input())

graph = {}  # defaultdict

for i in range(num_edge):
    n1, n2 = [int(i) for i in input().split()]
    if n1 not in graph:
        graph[n1] = []
    if n2 not in graph:
        graph[n2] = []
    graph[n1].append(n2)
    graph[n2].append(n1)

def bfs(graph, node):
    if node not in graph:
        return 0
    # for answer
    answer = []

    queue = deque()
    visited = [False] * (N+1)

    # start
    queue.append(node)
    visited[node] = True

    # loop
    while queue:
        node = queue.popleft()
        answer.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return len(answer)-1


print(bfs(graph, 1))