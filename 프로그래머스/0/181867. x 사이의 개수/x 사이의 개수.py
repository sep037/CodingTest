def solution(myString):
    answer = []
    count = 0
    for i in range(len(myString)):
        if myString[i] != 'x':
            count += 1
        else:
            answer.append(count)
            count = 0
    answer.append(count) #마지막에 x가 없는 경우도 추가 해줘야 하는 . .
    return answer