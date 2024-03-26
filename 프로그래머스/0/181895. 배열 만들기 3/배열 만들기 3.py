def solution(arr, intervals):
    answer = []
    for interval in intervals:
        i,j = interval
        for k in range(i,j+1):
            answer.append(arr[k])
        
    return answer