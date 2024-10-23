def min_operations_to_exceed_n(x, y, N):
    operations = 0
    while x <= N and y <= N:
        if x < y:
            x += y
        else:
            y += x
        operations += 1
    return operations

T = int(input())
for _ in range(T):
    A, B, N = map(int, input().split())  # x, y, N 입력
    print(min_operations_to_exceed_n(A, B, N))
