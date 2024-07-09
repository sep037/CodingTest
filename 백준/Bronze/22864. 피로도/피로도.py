import sys

input = sys.stdin.readline

A, B, C, M = map(int, input().split())


fatigue = 0
total_work = 0

for hour in range(24):
    if fatigue + A <= M:
        # 일을 할 수 있는 경우
        fatigue += A
        total_work += B
    else:
        # 쉬어야 하는 경우
        fatigue = max(0, fatigue - C)

print(total_work)