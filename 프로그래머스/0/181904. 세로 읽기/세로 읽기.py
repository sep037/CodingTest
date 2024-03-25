def solution(my_string, m, c):
    answer = ''
    num_rows = len(my_string) // m
    for i in range(num_rows):
        answer += my_string[i * m + c - 1]  # 인덱스는 0부터 시작하므로 c에서 1을 빼줌
    return answer
