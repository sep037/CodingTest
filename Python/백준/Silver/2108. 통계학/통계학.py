import sys

input = sys.stdin.readline

n = int(input())
number = []

for _ in range(n):
    num = int(input())
    number.append(num)

number.sort()

def get_average(arr, n):
    return round(sum(arr) / n)

def get_median(arr, n):
    return arr[n // 2]

def get_freq(arr):
    counts = dict()

    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    
    max_freq = max(counts.values())

    modes = []

    for num, freq in counts.items():
        if freq == max_freq:
            modes.append(num)
    
    modes.sort()
    
    if len(modes) > 1:
        return modes[1]
    return modes[0]

    
def get_gap(arr):
    max_val = max(arr)
    min_val = min(arr)
    return max_val - min_val

print(get_average(number, n))
print(get_median(number, n))
print(get_freq(number))
print(get_gap(number))