import sys
# sys.setrecursionlimit(10000)
# 이거 넣으면 되긴 함. 답은 ㅇㅇ 이해 완료
# 아래 코드 익히자

input = sys.stdin.readline

N, E = [int(i) for i in input().split()]
E_list = [input().split() for i in range(E)]

graph = {}
for i in range(N):
    graph[i+1] = []
for lst in E_list:
    u = int(lst[0])
    v = int(lst[1])

    graph[u].append(v)
    graph[v].append(u)

for k, v in graph.items():
    graph[k] = sorted(graph[k])

# dfs
def dfs(graph, node, visited):
    #print("> node :", node)
    visited[node-1] = True  # list index
    #print(visited)
    for next_node in graph[node]:
        if not visited[next_node-1]:
            dfs(graph, next_node, visited)
    return visited

cnt = 0
visited = [False] * len(graph)

while False in visited:
    cnt += 1
    node = visited.index(False) + 1
    dfs(graph, node, visited)

print(cnt)


###
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

input = sys.stdin.readline

# 입력 처리
N, E = map(int, input().split())
graph = defaultdict(list)

# 그래프 입력
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 함수
def dfs(graph, node, visited):
    visited[node] = True  # 1-based index 유지
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

# 연결 요소 개수 카운트
cnt = 0
visited = [False] * (N + 1)  # 1-based index 사용

for node in range(1, N + 1):
    if not visited[node]:  # 방문하지 않은 노드에서 DFS 시작
        cnt += 1
        dfs(graph, node, visited)

print(cnt)
