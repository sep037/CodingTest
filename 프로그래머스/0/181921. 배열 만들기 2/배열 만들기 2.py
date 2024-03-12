def solution(l, r):
    answer = []
    for i in range(l, r+1):
        a = str(i)
        if all(char in ['5', '0'] for char in a):
            answer.append(i)
    return answer if answer else [-1]