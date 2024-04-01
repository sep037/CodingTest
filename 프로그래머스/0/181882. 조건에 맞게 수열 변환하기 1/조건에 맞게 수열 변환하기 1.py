def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i]>=50:
            if arr[i]%2 == 0:
                answer.append(arr[i]/2)
            else:
                answer.append(arr[i])
        else:
            if arr[i]%2==1:
                answer.append(arr[i]*2)
            else:
                answer.append(arr[i])
    return answer