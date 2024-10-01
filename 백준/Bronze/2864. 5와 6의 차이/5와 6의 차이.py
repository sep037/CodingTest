# import sys

# input = sys.stdin.read
# A, B = input().split()

# def num_max(num1, num2):
#   for i in range(len(num1)):
#     if num1[i] == '5':
#       num1[i] = '6'
#     else:
#       continue
    
#   for j in range(len(num2)):
#     if num2[j] == '5':
#       num2[j] = '6'
#     else:
#       continue
# result = int(num1) + int(num2)
# print(result)
  
# def num_min(num1, num2):
#   for i in range(len(num1)):
#     if num1[i] == '6':
#       num1[i] = '5'
#     else:
#       continue
    
#   for j in range(len(num2)):
#     if num2[j] == '6':
#       num2[j] = '5'
#     else:
#       continue  
# answer = int(num1) + int(num2)
# print(answer)

  
# num_max(A,B)
# num_min(A,B)

# 처음에 코드 진짜 더럽게 짬
# .. 그래서 숫자 바꾸는 거 replace 함수 쓰려고요

A, B = input().split()

def num_max(num1, num2):
    # '5'를 '6'으로 바꾸는 작업
    max_num1 = num1.replace('5', '6')
    max_num2 = num2.replace('5', '6')
    return int(max_num1) + int(max_num2)

def num_min(num1, num2):
    # '6'을 '5'로 바꾸는 작업
    min_num1 = num1.replace('6', '5')
    min_num2 = num2.replace('6', '5')
    return int(min_num1) + int(min_num2)

print(num_min(A, B), num_max(A, B))
