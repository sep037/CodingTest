import sys

input = sys.stdin.readline

n = int(input().strip())  # 출입 기록의 수를 입력받음
log = [input().strip().split() for _ in range(n)]  # n개의 출입 기록을 입력받아 리스트에 저장

current_people = set()

for name, action in log:
    if action == "enter":
        current_people.add(name)  # 출근한 경우 집합에 추가
    elif action == "leave":
        current_people.discard(name)  # 퇴근한 경우 집합에서 제거

# 현재 회사에 있는 사람들을 사전 순으로 정렬하여 출력
for name in sorted(current_people, reverse=True):
    print(name)
