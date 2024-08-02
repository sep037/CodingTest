from collections import deque

def elevator(F, S, G, U, D):
    # 층의 범위를 벗어나면 도달할 수 없음
    if S == G:
        return 0
    
    # BFS를 위한 큐와 방문 기록을 위한 집합
    queue = deque([(S, 0)])
    visited = set([S])

    while queue:
        current, presses = queue.popleft()
        
        # 위로 U층 이동
        next_floor_up = current + U
        if next_floor_up == G:
            return presses + 1
        if next_floor_up <= F and next_floor_up not in visited:
            visited.add(next_floor_up)
            queue.append((next_floor_up, presses + 1))
        
        # 아래로 D층 이동
        next_floor_down = current - D
        if next_floor_down == G:
            return presses + 1
        if next_floor_down > 0 and next_floor_down not in visited:
            visited.add(next_floor_down)
            queue.append((next_floor_down, presses + 1))
    
    return "use the stairs"

# 입력을 받는 부분
F, S, G, U, D = map(int, input().split())
result = elevator(F, S, G, U, D)
print(result)
