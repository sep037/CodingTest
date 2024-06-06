def solution(arr, divisor):
    answer = []
    num = []
    count = 0
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
            count += 1
            
        else:
            continue
            count += 0
    if count == 0:
        return [-1]
    num = sorted(answer)
    return num