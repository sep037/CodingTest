def max_weight(ropes):
    ropes.sort(reverse=True)  # 로프를 내림차순 정렬
    max_w = 0
    
    for i in range(len(ropes)):
        # i번째 로프까지 사용할 때 들어올릴 수 있는 최대 중량 계산
        max_w = max(max_w, ropes[i] * (i + 1))
    
    return max_w

N = int(input())
ropes = []

for _ in range(N): # 로프의 최대 중량 입력
    weight = int(input())
    ropes.append(weight)

print(max_weight(ropes))
