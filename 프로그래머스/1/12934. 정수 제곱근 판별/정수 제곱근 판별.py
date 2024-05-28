def solution(n):
    answer = -1
    i = 1
    while i * i <= n:
        if i * i == n:
            answer = (i + 1) * (i + 1)
            break
        i += 1
    return answer
