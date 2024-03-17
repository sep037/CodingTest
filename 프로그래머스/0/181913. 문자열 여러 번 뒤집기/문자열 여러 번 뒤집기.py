def solution(my_string, queries):
    for query in queries:
        s,e = query
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
        #슬라이싱 [시작인덱스:끝인덱스] + 근데 끝 인덱스는 포함이 안됨 ! 실제로는 끝인덱스-1까지만
    return my_string
