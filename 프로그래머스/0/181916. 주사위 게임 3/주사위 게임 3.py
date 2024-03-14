def solution(a, b, c, d):
    answer = 0
    dice = [a,b,c,d]
    counts = [dice.count(i) for i in dice]
    if max(counts) == 4:
        answer += a*1111
    elif max(counts) == 3:
        p = dice[counts.index(3)]
        q = dice[counts.index(1)]
        answer += (10*p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2 :
            if a == b:
                answer += (a+c)*abs(a-c)
            elif a == c:
                answer += (a+b)*abs(a-b)
            else :
                answer += (a+c)*abs(a-c)
        else: 
            r = dice[counts.index(2)]
            answer += (a*b*c*d)/r**2
    elif max(counts)  == 1:
        answer += min(dice)
    return answer