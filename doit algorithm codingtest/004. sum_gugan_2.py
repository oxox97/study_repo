# 2차원 구간 합
# prefix_sum -> psum

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]  # 0-based mat

psum_mat = [[0] * (N+1) for _ in range(N+1)]  # 1-based mat

# 누적합 계산
for y in range(N):
    for x in range(N):
        psum_mat[y+1][x+1] = (
            psum_mat[y+1][x] + psum_mat[y][x+1]
            - psum_mat[y][x] + mat[y][x]
        ) # psum_mat은 1-based index라서 [r+1][c+1]이 아닌, [r][c]
        
answer = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())  # [y][x] ...? 왜지?
    a = psum_mat[x2][y2] - psum_mat[x2][y1-1] - psum_mat[x1-1][y2] + psum_mat[x1-1][y1-1]
    answer.append(a)

for a in answer:
    print(a)