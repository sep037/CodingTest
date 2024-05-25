# CodingTest
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).


# BOJ IO

```python
input() # 한 줄의 문자열을 입력
map() # 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

data = list(map(int, input().split())) # 공백을 기준으로 구분된 데이터를 입력 받을 때
a, b, c = map(int, input().split()) # 공백을 기준으로 구분된 데이터가 많지 않을 때

sys.stdin = open("input.txt","r") # 파일 입출력

# 좀 더 빠르게 입력 받기 !
import sys
input = sys.stdin.readline() # 입력 후 엔터가 사용되므로 rstrip()을 함께 사용하기
N, M = map(int, input.split()) 
board = [list(map(int, input.split())) for _ in range(N)] # 2차원 리스트 입력 받기
data = input().rstrip() # 문자열 입력 받기
```

어우 귀찮아
