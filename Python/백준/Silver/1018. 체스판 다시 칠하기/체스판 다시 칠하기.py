M, N = map(int, input().split())
board = [input() for _ in range(M)]

pattern1 = [
    "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
    "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"
]
pattern2 = [
    "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
    "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"
]

min_paint = 64

for i in range(M - 7):
    for j in range(N - 7):
        draw1 = 0
        draw2 = 0

        for r in range(8):
            for c in range(8):
                if board[i+r][j+c] != pattern1[r][c]:
                    draw1 += 1
                if board[i+r][j+c] != pattern2[r][c]:
                    draw2 += 1

        current_min = min(draw1, draw2)
        if current_min < min_paint:
            min_paint = current_min

print(min_paint)