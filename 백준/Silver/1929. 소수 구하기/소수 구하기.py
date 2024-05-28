import sys

input = sys.stdin.readline

S, E = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1): #제곱근까지 확인
        if num % i == 0:
            return False
    return True

num = []

for i in range(S, E + 1):
    if is_prime(i):
        num.append(i)

for j in num:
    print(j)
