from collections import deque
import sys
input = sys.stdin.readline

# 덱 생성
dq = deque()

def process_command(command):
    cmd = command.split()
    
    if cmd[0] == "1":
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == "2":
        dq.append(int(cmd[1]))
    elif cmd[0] == "3":
        print(dq.popleft() if dq else -1)
    elif cmd[0] == "4":
        print(dq.pop() if dq else -1)
    elif cmd[0] == "5":
        print(len(dq))
    elif cmd[0] == "6":
        print(1 if not dq else 0)
    elif cmd[0] == "7":
        print(dq[0] if dq else -1)
    elif cmd[0] == "8":
        print(dq[-1] if dq else -1)

n = int(input())
for _ in range(n):
    process_command(input().strip())
