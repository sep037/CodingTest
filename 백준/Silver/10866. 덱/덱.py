from collections import deque
import sys
input = sys.stdin.read

# 덱 생성
dq = deque()

commands = input().splitlines()

# 명령 처리 함수
def process_command(command):
    if command.startswith("push_front"):
        _, value = command.split()
        dq.appendleft(int(value))
    elif command.startswith("push_back"):
        _, value = command.split()
        dq.append(int(value))
    elif command == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(dq))
    elif command == "empty":
        print(1 if not dq else 0)
    elif command == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)

for command in commands:
    process_command(command)
