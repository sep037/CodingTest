def solution(hp):
    answer = 0
    ant = [5,3,1]
    for i in range(len(ant)):
        answer += hp//ant[i]
        hp = hp - ant[i]*(hp//ant[i])
    return answer