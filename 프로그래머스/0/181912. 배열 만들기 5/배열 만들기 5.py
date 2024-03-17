def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        intStr = int(intStr[s:s+l])
        if intStr>k:
            answer.append(intStr)
        else:
            continue
        
    return answer