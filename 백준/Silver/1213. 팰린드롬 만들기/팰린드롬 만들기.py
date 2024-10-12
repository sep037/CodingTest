# 팰린드롬은 앞에서 순서를 거꾸로 읽었을 때도 원래의 문자열이나 수열과 동일한 경우 !
# + 정답이 여러 개가 되는 경우에는 사전 순으로 앞서는 것을 출력하기 !
# 반으로 나눠서 비교해야하나 ..? 문자열의 앞쪽과 뒤쪽 절반을 비교하여 모든 문자가 동일한지 확인

from collections import Counter
# 이거 빈도수 계산하는 거 처음 써보는데
# from collections import Counter

# # 문자열의 각 문자의 빈도수를 계산
# name = "hahaaha"
# count = Counter(name)

# print(count)
# 이렇게 하면 
# Counter({'h': 3, 'a': 4})
# 이렇게 나온다구 함

def make_palindrome(name):
    # 그래서 알파벳마다 빈도수를 계산해준다
    count = Counter(name)
    
    # 홀수 개수의 문자가 몇 개인지 확인
    odd_count = 0
    odd_char = ''
    for char, freq in count.items():
        if freq % 2 != 0:
            odd_count += 1
            odd_char = char
    
    # 홀수인 문자의 개수가 2개 이상이면 팰린드롬 만들 수 없음
    # 왜냐하면 대칭이 안되니까 !
    if odd_count > 1:
        return "I'm Sorry Hansoo"
    
    #팰린드롬의 앞뒤 절반 만들기 -> 정렬 필요함
    first_half = []
    for char, freq in sorted(count.items()):
        first_half.append(char * (freq // 2))
    
    # 팰린드롬 완성
    first_half = ''.join(first_half)
    second_half = first_half[::-1]  # 뒤집어서 두 번째 절반 만들기 -> 왜냐면 똑같은 거 만들어야 하니까
    palindrome = first_half + odd_char + second_half
    
    return palindrome

name = input().strip()
print(make_palindrome(name))
