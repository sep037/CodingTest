def solution(arr1, arr2):
    # 행렬 초기화
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):  # arr1의 행을 순차적으로 처리
        for j in range(len(arr2[0])):  # arr2의 열
            for k in range(len(arr2)):  # arr2의 행
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result
