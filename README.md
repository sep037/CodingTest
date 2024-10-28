# CodingTest
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).


# BOJ IO

```python
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제

data = list(map(int, input().split())) # 공백을 기준으로 구분된 데이터를 입력 받을 때
a, b, c = map(int, input().split()) # 공백을 기준으로 구분된 데이터가 많지 않을 때

sys.stdin = open("input.txt","r") # 파일 입출력

import sys
input = sys.stdin.readline() # 입력 후 엔터가 사용되므로 rstrip()을 함께 사용하기
N, M = map(int, input.split()) 
board = [list(map(int, input.split())) for _ in range(N)] # 2차원 리스트 입력 받기
data = input().rstrip() # 문자열 입력 받기
```

어우 귀찮아
