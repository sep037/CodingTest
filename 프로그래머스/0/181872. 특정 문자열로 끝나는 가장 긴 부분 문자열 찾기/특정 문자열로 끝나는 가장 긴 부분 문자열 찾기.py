def solution(myString, pat):
    answer = ''
    length = len(pat)
    for i in range(len(myString)):
        if myString[i] == pat[length-1]:
            idx = i
    answer = myString[:idx+1]
    return answer