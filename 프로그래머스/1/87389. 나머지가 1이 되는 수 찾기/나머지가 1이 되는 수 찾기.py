def solution(n):
    answer = 0
    num = []
    for i in range(n):
        if i == 0:
            continue
        elif n%i == 1:
            num.append(i)
        else:
            continue
    answer = min(num)
    return answer