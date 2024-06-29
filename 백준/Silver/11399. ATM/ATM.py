import sys

input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
P = list(map(int, data[1].split()))  # 각 사람이 돈을 인출하는 데 걸리는 시간

P.sort()

total_time = 0
waiting_time = 0

for time in P:
    waiting_time += time  # 이전 사람들이 기다리는 시간 누적
    total_time += waiting_time  # 현재 사람이 돈을 인출하는데 필요한 시간 누적

print(total_time)
