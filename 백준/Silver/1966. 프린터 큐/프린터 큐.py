from collections import deque

def printer(test_cases):
    results = []
    for case in test_cases:
        n, m = case['n'], case['m']
        priorities = case['priorities']

        queue = deque([(i, priorities[i]) for i in range(n)])
        count = 0

        while queue:
            current = queue.popleft()

            if any(current[1] < item[1] for item in queue):
                queue.append(current)
            else:
                count += 1
                if current[0] == m:
                    results.append(count)
                    break
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    test_cases.append({'n': n, 'm': m, 'priorities': priorities})

results = printer(test_cases)
for res in results:
    print(res)
