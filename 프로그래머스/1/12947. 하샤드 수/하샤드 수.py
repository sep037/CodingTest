def solution(x):
    answer = True
    x2 = str(x)
    num = 0
    for i in range(len(x2)):
        num += int(x2[i])
    if x%num == 0:
        answer = True
    else:
        answer = False
    return answer