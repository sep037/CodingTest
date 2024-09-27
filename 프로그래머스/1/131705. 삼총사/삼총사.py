def solution (number) :
    from itertools import combinations
    # itertools 라이브러리 사용
    cnt = 0
    for i in combinations(number,3) :
        # 주어진 배열 요소들 전체 중에서 3개 뽑아서 더한 게 0이 되는지 확인
        if sum(i) == 0 :
            cnt += 1
            # 0이면 cnt +1
    return cnt