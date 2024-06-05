def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        b = min(arr)
        arr.remove(b)
        return arr
