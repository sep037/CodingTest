def solution(my_string, alp):
    answer = ''
    answer = my_string.lower()
    alp2 = alp.upper()
    answer = answer.replace(alp, alp2)
    return answer