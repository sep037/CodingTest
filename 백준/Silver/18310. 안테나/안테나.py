n = int(input())
antenna = list(map(int, input().split()))
antenna.sort()

print(antenna[(n-1)//2])