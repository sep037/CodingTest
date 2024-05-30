#일단 최소가 되려면 가장 큰 값과 가장 작은 값을 곱하여 더하면 바로 찾을 수 있지 않을까요리
#그럼 그냥 배열 하나 내림차순으로 하고 나머지 하나를 오름차순으로 정렬하고 걍 인덱스 같은 것끼리 곱해서 누적합 구하면 되겠네요 ~~
def solution(A,B):
    arr_A = sorted(A, reverse = False)
    arr_B = sorted(B, reverse = True)
    answer = 0
    
    for i in range(len(A)): #어차피 길이 똑가틈
        answer += arr_A[i] * arr_B[i]

    return answer