import sys

input = sys.stdin.readline
K = int(input().strip()) 
answer = 0
data = [input().strip() for _ in range(2 * K)]


data_dg = data[:K]
data_ys = data[K:]

entry_order = {car: i for i, car in enumerate(data_ys)}

# 대근이의 목록을 순서대로 탐색하면서 추월 여부를 확인
max_exit_order = -1  # 현재까지 탐색된 차량들 중 가장 빨리 나간 차량의 순서

for car in data_dg:
    if entry_order[car] > max_exit_order:
        max_exit_order = entry_order[car]
    else:
        answer += 1

print(answer)
