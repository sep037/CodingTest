def solution(arr, idx):
    answer = -1
    for i,val in enumerate(arr):
        if i>=idx:
            if arr[i] == 1:
                answer = i
                break
            elif i == len(arr)-1:
                return answer
    return answer