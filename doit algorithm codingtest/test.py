# 2차원 구간 합
# prefix_sum -> psum

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]  # 0-based mat

psum_mat = [[0] * (N+1) for _ in range(N+1)]  # 1-based mat

for r in range(N):
    for c in range(N):
        psum_mat[r+1][c+1] = (
            psum_mat[r+1][c] + psum_mat[r][c+1]
            - psum_mat[r][c] + mat[r][c]
        ) # psum_mat은 1-based index라서 [r+1][c+1]이 아닌, [r][c]
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    a = psum_mat[x2][y2] - psum_mat[x2][y1-1] - psum_mat[x1-1][y2] + psum_mat[x1-1][y1-1]
    print(a)