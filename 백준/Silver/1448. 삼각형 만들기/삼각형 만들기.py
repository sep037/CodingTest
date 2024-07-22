import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
triangle = list(map(int, data[1:]))

# 삼각형이 만들어지는 조건은 긴 변을 제외한 두 변의 합 >= 가장 긴 변
triangle.sort(reverse=True)

answer = -1
for i in range(N-2):  # 세 변을 선택하기 위해 N-2까지 반복
    if triangle[i] < triangle[i+1] + triangle[i+2]: 
        answer = triangle[i] + triangle[i+1] + triangle[i+2] 
        break  # 조건 만족 시 반복 종료

print(answer) 