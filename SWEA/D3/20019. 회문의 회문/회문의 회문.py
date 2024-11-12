def is_palindrome(s): # 문자열 전체가 회문인지 확인 !
    return s == s[::-1]

def is_palindrome_of_palindrome(s): # 회문의 회문인지 확인 !
    n = len(s)
    if not is_palindrome(s):
        return False
    
    mid = (n - 1) // 2
    first_half = s[:mid]
    second_half = s[mid+1:]
    
    return is_palindrome(first_half) and is_palindrome(second_half)

T = int(input())
results = []

for t in range(1, T + 1):
    s = input().strip()
    if is_palindrome_of_palindrome(s):
        results.append(f"#{t} YES")
    else:
        results.append(f"#{t} NO")

print("\n".join(results))
