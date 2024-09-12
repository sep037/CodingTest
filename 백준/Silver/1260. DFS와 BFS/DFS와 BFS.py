from collections import deque

def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')  # 방문한 노드를 출력

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True  # 시작 노드를 방문 처리

    while queue:
        v = queue.popleft()
        print(v, end=' ')  # 방문한 노드를 출력

        # 현재 노드와 연결된 다른 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, S = map(int, input().split())  # N: 정점 수, M: 간선 수, S: 시작 노드
graph = [[] for _ in range(N+1)]  # 인접 리스트 초기화

# 간선 정보 입력 받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)  # 방문 기록 초기화
dfs(graph, S, visited)
print()

visited = [False] * (N+1)  # 방문 기록 초기화
bfs(graph, S, visited)  # BFS 탐색 결과 출력
