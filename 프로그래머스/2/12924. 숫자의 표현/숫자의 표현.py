def solution(n):
    count = 0  # 방법의 수를 저장할 변수
    m = 1  # 연속된 자연수의 개수를 나타내는 변수

    while (m * (m - 1)) // 2 < n:
        if (n - (m * (m - 1)) // 2) % m == 0:
            count += 1
        m += 1

    return count
