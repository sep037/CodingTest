import sys
input = sys.stdin.readline

N = int(input().strip())
# 상근이가 가진 숫자 카드의 숫자들
data = set(map(int, input().strip().split()))

M = int(input().strip())
# 확인하고 싶은 숫자들
queries = list(map(int, input().strip().split()))

answer = []

# 각 쿼리에 대해 상근이가 해당 숫자 카드를 가지고 있는지 확인
for query in queries:
    if query in data:
        answer.append(1)
    else:
        answer.append(0)

print(" ".join(map(str, answer)))