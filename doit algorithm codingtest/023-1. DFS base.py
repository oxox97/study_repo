# DFS 개념 연습

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

answer = [0, 1, 3, 4, 5, 2]

# 1. 재귀 (recursion)

def dfs_recursion(node):
    visited[node] = True
    print(node, end = " ")
    for next_node in sorted(graph[node]):
        if not visited[next_node]:
            dfs_recursion(next_node)
    # print(f"Backtrack from: {node}")

    
visited = [False] * len(graph)
# dfs_recursion(0)

# 2. 스택 (stack)
def dfs_stack(node):
    stk.append(node)

    while stk:
        node = stk.pop()

        if visited[node]:
            continue

        print(node, end=' > ')  # 방문 노드 출력
        visited[node] = True

        for neighbor in sorted(graph[node], reverse=True):
            if not visited[neighbor]:
                stk.append(neighbor)

stk = []
visited = [False] * (len(graph)+1)  # due to case of 1-based index
dfs_stack(0)
