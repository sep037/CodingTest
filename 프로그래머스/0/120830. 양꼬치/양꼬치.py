def solution(n, k):
    answer = 0
    d = n // 10
    answer = n*12000 + (k-d)*2000
    return answer