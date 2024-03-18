def solution(my_string, n):
    answer = ''
    r = len(my_string)
    answer += my_string[r-n:]
    return answer