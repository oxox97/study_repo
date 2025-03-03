# 해당 방식으로 이해 완료
# 추후, 스택과 큐에 들어갈 때 visited 체크해서 중복 노드 막는 방식 생각 (보다 효율적, 지금 방식이 틀린 건 아님)

from collections import deque

N, M, node = [int(i) for i in input().split()]
# node : start node

graph = dict()
for i in range(1,N+1):
    graph[i] = []

for _ in range(M):
    n1, n2 = [int(i) for i in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)  # 양방향 간선

def dfs_using_stack(graph, node):
    # define
    stk = []
    visited = [False] * (N+1)  # 1-based index

    # initial node
    stk.append(node)

    # dfs
    """
    방문하지 않은 노드만 스택에 쌓음
    주의) 출력을 방문으로 보기 때문에 스택에 같은 노드가 2개 이상 들어갈 수 있음!
    """
    while stk:
        node = stk.pop()
        if not visited[node]:  # top 노드가 방문하지 않은 노드일 때,
            print(node, end=" ")  # 출력
            visited[node] = True  # 그리고 방문 체크
            for neighbor in sorted(graph[node], reverse=True):  # 값이 작은 노드 먼저 방문
                stk.append(neighbor)

def bfs_using_queue(graph, node):
    # define
    queue = deque()
    visited = [False] * (N+1)

    # initial node
    queue.append(node)

    # bfs
    """
    방문하지 않은 노드만 큐에 쌓음
    dfs 스택과 node 할당 부분 빼고 다 동일
    """
    while queue:
        node = queue.popleft()
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True
            for neighbor in sorted(graph[node], reverse=False):  # queue는 fifo이므로 값이 작은 노드 먼저 방문하려면 stack과 정렬 기준 반대
                queue.append(neighbor)

# 추가
def dfs_using_recursion(graph, visited, node):
    visited[node] = True
    print(node, end=" ")

    for neighbor in sorted(graph[node]):
        if not visited[neighbor]:
            dfs_using_recursion(graph, visited, neighbor)

    

dfs_using_stack(graph, node)
print()
visited = [False] * (N+1)
dfs_using_recursion(graph, visited, node)
print()
bfs_using_queue(graph, node)