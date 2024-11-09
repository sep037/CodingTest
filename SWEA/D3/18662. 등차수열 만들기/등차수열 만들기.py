T = int(input())
results = []

for _ in range(T):
    a, b, c = map(int, input().split())
    
    # a를 변경하는 경우
    x1 = abs(2 * b - c - a)
    # b를 변경하는 경우
    x2 = abs((a + c) / 2 - b)
    # c를 변경하는 경우
    x3 = abs(2 * b - a - c)
    
    # 최소값 계산
    min_x = min(x1, x2, x3)
    results.append(f"{min_x:.1f}")

# 결과 출력
for i, result in enumerate(results, 1):
    print(f"#{i} {result}")
