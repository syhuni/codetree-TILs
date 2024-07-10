import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# dp 초기조건
dp[0][0] = 1
for i in range(1, n):
    if grid[i][1] > grid[0][0]:
        dp[i][1] = 2 
for j in range(1, m):
    if grid[1][j] > grid[0][0]:
        dp[1][j] = 2

for i in range(2, n):
    for j in range(2, m):
        if grid[i][j] <= grid[0][0]:
            continue

        dp[i][j] = 2
        for k in range(1, j):  # i, j의 왼쪽 위 한 줄 확인
            if not dp[i - 1][k]:
                continue

            if grid[i][j] > grid[i - 1][k]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + 1)

# 최댓값 찾기
max_val = 1
for i in range(n):
    for j in range(m):
        max_val = max(max_val, dp[i][j])

print(max_val)