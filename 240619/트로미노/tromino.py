'''
바깥쪽을 0으로 채우고 가운데를 중심으로 십자 모양, 가운데와 가운데 제외 2개의 합 최대
'''
def sum_cal(row, col):
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    cal_lst = []
    for k in range(4):
        cal_lst.append(grid[row + di[k]][col + dj[k]])
    cal_lst.sort(reverse=True)
    return grid[row][col] + sum(cal_lst[:2])

n, m = map(int, input().split())

grid = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
extra_row = [[0] * (m + 2)]
grid = extra_row + grid + extra_row

max_sum = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        result = sum_cal(i, j)
        max_sum = max(max_sum, result)

print(max_sum)