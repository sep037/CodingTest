def solution(arr, queries):
    for query in queries:
        s,e = query
        for i in range(len(arr)):
            if i >=s and i <= e:
                arr[i] += 1
    return arr