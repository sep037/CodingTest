TC = int(input())
test_cases = [int(input()) for _ in range(TC)]

def multiplication(N):
    for i in range(1, 10):
        if N % i == 0:
            j = N // i
            if 1 <= j <= 9:
                return "Yes"
    return "No"


for idx, N in enumerate(test_cases, 1):
    result = multiplication(N)
    print(f"#{idx} {result}")
