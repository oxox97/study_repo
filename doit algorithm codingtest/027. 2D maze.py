# 지나야 하는 최소의 칸 수 -> BFS 이용한 최단 경로
# 2D 이므로 4방향 탐색
# BFS 이므로 queue (deque)
# 갈 때마다 dist + 1
# 조건은
# 1. 갈 수 있는 길이고 (=1)
# 2. 안 갔던 길이며 (=visitied False)
# 3. 퍼즐 범위 안에 있어야 함 (넘어가면 리스트 오버? 됨)

from collections import deque

N, M = map(int, input().split())

maze = [list(map(int, input())) for i in range(N)]

# define
visited = [[False] * (M) for i in range(N)]
x, y = 0, 0
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상하좌우
dist = [[0] * (M) for _ in range(N)]  # 놓쳤음 1)
dist[0][0] = 1  # 놓쳤음 2)

def bfs_2d(maze, visited, x, y, dist):
    # initial
    queue = deque([[y, x]])
    visited[y][x] = True
    print(f"> START : {[y, x]}")

    # loop
    while queue:
        print(queue)
        y, x = queue.popleft()
        if y == N-1 and x == M-1:
            return dist[y][x]
        for dy, dx in directions:            
            ny = y + dy
            nx = x + dx
            if 0 <= ny <= (N-1) and 0 <= nx <= (M-1) and maze[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                print(f"\n> ROUTE : {[ny, nx]}")
                queue.append([ny, nx])
                dist[ny][nx] = dist[y][x] + 1

answer = bfs_2d(maze, visited, x, y, dist)
print(answer)
