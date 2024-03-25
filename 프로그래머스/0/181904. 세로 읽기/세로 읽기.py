def solution(my_string, m, c):
    answer = ''
    num_rows = len(my_string) // m
    for i in range(num_rows):
        answer += my_string[i * m + c - 1]
    return answer
