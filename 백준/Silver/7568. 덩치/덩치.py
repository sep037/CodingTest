def calculate_ranks(bodies):
    N = len(bodies)
    ranks = [1] * N

    # 모든 사람들끼리 비교
    for i in range(N):
        for j in range(N):
            if i != j:
                # i번 사람보다 j번 사람이 더 크면 i번 사람의 등수 증가
                if bodies[i][0] < bodies[j][0] and bodies[i][1] < bodies[j][1]:
                    ranks[i] += 1

    return ranks


N = int(input())
bodies = []

for _ in range(N):
    x, y = map(int, input().split())
    bodies.append((x, y))  # (몸무게, 키) 튜플로 저장

ranks = calculate_ranks(bodies)

# 공백으로 구분
print(" ".join(map(str, ranks)))
