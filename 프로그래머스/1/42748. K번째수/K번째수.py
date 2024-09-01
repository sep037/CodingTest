def solution(array, commands):
    answer = []
    for command in commands:
        start, end, k = command[0], command[1], command[2]
        sliced_array = sorted(array[start-1:end])
        answer.append(sliced_array[k-1])
    return answer
