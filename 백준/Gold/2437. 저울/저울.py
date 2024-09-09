# N = int(input())

# weights = []
# for _ in range(N):
#     weights.append(int(input()))

# weights.sort()

# answer = 1

# for weight in weights:
#     if weight > answer:
#         break # 현재 추가 지금까지 만들 수 있는 범위를 넘으면 그 값이 만들 수 없는 첫 번째 무게
#     answer += weight

# print(answer)

# 이렇게 풀었더니 런타임에러 뜸
# ;; 입력에 문제가 있나 입력 수정 해봄

import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))

weights.sort()

answer = 1

for weight in weights:
    if weight > answer:
        break # 현재 추가 지금까지 만들 수 있는 범위를 넘으면 그 값이 만들 수 없는 첫 번째 무게
    answer += weight

print(answer)

