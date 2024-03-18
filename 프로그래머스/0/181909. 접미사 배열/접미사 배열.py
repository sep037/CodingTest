def solution(my_string):
    answer = []
    e = len(my_string)
    s = 0
    while s < e:
        answer.append(my_string[s:])
        s+=1
        #파이썬 사전순으로 정렬 .sort()
        answer.sort()
    return answer