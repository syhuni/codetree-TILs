import sys
input = sys.stdin.readline

def coin_counter(row, col):
    coin_count = 0
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            coin_count += grid[r][c]
    return coin_count


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0

for i in range(N - 2):
    for j in range(N - 2):
        result = coin_counter(i, j)
        max_cnt = max(max_cnt, result)

print(max_cnt)