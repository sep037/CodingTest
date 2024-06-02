def solution(n):
    answer = ''
    num = n//2
    if n%2 == 1:
        for i in range(num):
            answer += '수박'
        return answer + '수'
    elif n == 0:
        answer = ''
    else:
        for i in range(num):
            answer += '수박'
            
    return answer