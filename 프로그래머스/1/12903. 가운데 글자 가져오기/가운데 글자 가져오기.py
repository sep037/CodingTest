def solution(s):
    answer = ''
    num = len(s) // 2
    if len(s) % 2 == 0:
        answer = s[num-1:num+1]
    else:
        answer = s[num]
    return answer
