def solution(name, yearning, photo):
    answer = []
    for people in photo:
        score = 0
        for n in people:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)
    return answer