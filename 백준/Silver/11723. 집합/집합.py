import sys
input = sys.stdin.readline

S = set()

def process_command(command):
    global S
    if command.startswith("add"):
        _, x = command.split()
        S.add(int(x))  # 집합에 원소 추가
    elif command.startswith("remove"):
        _, x = command.split()
        S.discard(int(x))  # 집합에서 원소 제거 (없으면 무시)
    elif command.startswith("check"):
        _, x = command.split()
        print(1 if int(x) in S else 0)  # 원소가 있으면 1, 없으면 0 출력
    elif command.startswith("toggle"):
        _, x = command.split()
        x = int(x)
        if x in S:
            S.remove(x)  # 있으면 제거
        else:
            S.add(x)  # 없으면 추가
    elif command == "all":
        S = set(range(1, 21))
    elif command == "empty":
        S.clear()  


N = int(input())  
for _ in range(N):
    process_command(input().strip())  
