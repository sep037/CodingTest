def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    
    while i <= j:
        # 가장 가벼운 사람과 가장 무거운 사람을 같이 태울 수 있는지 확인
        if people[i] + people[j] <= limit:
            i += 1  # 가벼운 사람 태움
        # 무거운 사람은 항상 태움
        j -= 1
        boats += 1
        
    return boats
