import sys

input = sys.stdin.readline

N, M = map(int, input().split()) 
set_S = set(input().strip() for _ in range(N))  # N개의 문자열을 집합 S에 저장
count = 0

for _ in range(M):
    string = input().strip()  # M개의 문자열을 하나씩 입력받아 string에 저장
    if string in set_S:  # string이 집합 S에 포함되어 있는지 확인
        count += 1

print(count)  # 포함된 문자열의 개수를 출력
