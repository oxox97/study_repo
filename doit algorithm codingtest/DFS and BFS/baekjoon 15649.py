
# 중복되는 수열을 여러 번 출력하며 안 되며 -> visited 
# 수열은 사전 순으로 증가하는 순서로 출력 -> sorted(graph[node])

# ⭐️"모든 수열"을 찾는 것은 DFS 중 "재귀"를 사용해야 함 (for "백트래킹")⭐️
# 해당 문제는 그래프 필요없는 문제

N, M = [int(i) for i in input().split()]

def dfs(node, visited):

    answer.append(node)
    visited[node] = True

    if len(answer) == M:
        for a in answer:
            print(a, end=" ")
        print()

    for neighbor in range(1, N+1):
        if not visited[neighbor]:
            dfs(neighbor, visited)

            # ⭐️ 백트래킹 핵심
            answer.pop()
            visited[neighbor] = False  # 백트래킹 : 다시 방문 가능하도록

for i in range(1, N+1):
    visited = [False] * (N+1)
    answer = []
    dfs(i, visited)