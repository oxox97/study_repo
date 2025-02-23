# BFS 개념 연습

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# answer = [0, 1, 3, 4, 5, 2] : dfs
answer = [0, 1, 2, 3, 4, 5]  # bfs

from collections import deque

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in sorted(graph[node]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True  # 중복 방문 방지하기 위해 append 시 방문했다고 간주!

visited = [False] * len(graph)
bfs(0)
