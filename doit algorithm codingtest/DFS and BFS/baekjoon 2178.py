# 미로 탐색 (핵심 유형인듯)

# 내 생각
# 미로니까 dfs -> 최단거리 미로니까 BFS인듯?! -> 틀린 길을 찾을수도 있어 DFS는 비효율적이고, 최단거리 미로는 BFS (외)
# 그래프 정의 필요

# 모든 경우의 수 : dfs의 백트래킹
# 최단 거리 : bfs

from collections import deque

# N, M = [int(i) for i in input().split()]

# 2D 그래프 정의
# 힌트 : grid[y][x]
# 상 하 좌 우 이동 표현
# 행렬은 왼쪽 위가 (1,1) 이기 때문에 위로 가려면 y축 감소임.. 그래프랑 다름
# [x][y]가 아닌 이유는 행렬이라서
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(start_y, start_x):
    queue = deque()
    queue.append((start_y, start_x, 1))  # (y, x, 현재 거리)
    visited[start_y][start_x] = True

    while queue:
        y, x, dist = queue.popleft()

        # 목표 도착 시 거리 반환
        if y == N-1 and x == M-1:
            return dist
        
        # 네 방향 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위 안에 있고, 방문 안 했고, 길이 있으면 이동
            # ✅ 조건 1: 미로 범위를 벗어나지 않음
            # ✅ 조건 2: 아직 방문하지 않음
            # ✅ 조건 3: 벽(0)이 아니라 길(1)
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and maze[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((ny, nx, dist+1))  # 거리 +1
        
    return -1

maze = [
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1]
]

N = len(maze)
M = len(maze[0])
visited = [[False] * M for _ in range(N)]

shortest_path = bfs(0, 0)
print(shortest_path)