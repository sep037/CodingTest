import sys

input = sys.stdin.readline

N, M = map(int, input().split())

poketmon_by_number = [input().strip() for _ in range(N)]
poketmon_by_name = {name: str(index + 1) for index, name in enumerate(poketmon_by_number)}

questions = [input().strip() for _ in range(M)]

for question in questions:
    if question.isdigit():
        # 숫자인 경우
        print(poketmon_by_number[int(question) - 1])
    else:
        # 문자인 경우
        print(poketmon_by_name[question])
