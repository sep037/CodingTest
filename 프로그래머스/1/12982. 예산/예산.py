def solution(d, budget):
    count = 0
    d.sort() 
    for i in range(len(d)):
        if budget >= d[i]:  # 현재 부서의 요청 금액을 지원할 수 있을 때
            budget -= d[i]
            count += 1
        else:  # 예산이 부족해질 경우, 더 이상 진행 x
            break
    return count
