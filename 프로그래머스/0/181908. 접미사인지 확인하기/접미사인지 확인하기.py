def solution(my_string, is_suffix):
    answer = []
    e = len(my_string)
    s = 0
    while s < e:
        answer.append(my_string[s:])
        s+=1
    if is_suffix in answer:
        return 1
    else: return 0

