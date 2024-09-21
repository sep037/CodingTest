n = int(input()) 
commands = [input().strip() for _ in range(n)]

def stackfunc(commands):
    stack = []
    results = []

    for command in commands:
        if command.startswith('push'):
            _, x = command.split()
            stack.append(int(x))
        elif command == 'pop':
            if stack:
                results.append(stack.pop())
            else:
                results.append(-1)
        elif command == 'size':
            results.append(len(stack))
        elif command == 'empty':
            results.append(1 if not stack else 0)
        elif command == 'top':
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)
    
    return results

results = stackfunc(commands)
for result in results:
    print(result)
