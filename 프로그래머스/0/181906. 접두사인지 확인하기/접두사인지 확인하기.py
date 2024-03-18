def solution(my_string, is_prefix):
    answer = []
    s = 0
    e = len(my_string)
    while s<e:
        answer.append(my_string[s:e])
        e -= 1
    if is_prefix in answer:
        return 1
    else: 
        return 0