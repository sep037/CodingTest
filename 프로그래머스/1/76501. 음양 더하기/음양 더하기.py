def solution(absolutes, signs):
    answer = []
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == 1 :
            answer.append(absolutes[i])
        else:
            answer.append(absolutes[i]*(-1))
    for k in range(len(answer)):
        result += answer[k]
    return result