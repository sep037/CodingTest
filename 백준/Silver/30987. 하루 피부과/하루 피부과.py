x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

def calculate(x1, x2, a, b, c, d, e):
    A = a
    B = b - d
    C = c - e

    def integral(x):
        return (A * x**3) / 3 + (B * x**2) / 2 + C * x
    
    result = integral(x2) - integral(x1)
    return int(result)

laser_intensity = calculate(x1, x2, a, b, c, d, e)
print(laser_intensity)
