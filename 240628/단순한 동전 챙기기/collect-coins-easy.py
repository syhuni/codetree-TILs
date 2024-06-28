import sys
input = sys.stdin.readline


def find_min(cnt, idx, loc_tuple, val):
    global min_val
    if cnt == 3:
        i, j = loc_tuple
        ni, nj = start_end_loc_lst[1][1]  # End 좌표
        val += abs(i - ni) + abs(j - nj)
        min_val = min(min_val, val)
        return

    if idx == len(nums_loc_lst):
        return

    i, j = loc_tuple
    # nums_loc_lst[idx][1] == i좌표, nums_loc_lst[idx][2 == j좌표
    find_min(cnt + 1, idx + 1, (nums_loc_lst[idx][1], nums_loc_lst[idx][2]), 
            val + abs(i - nums_loc_lst[idx][1]) + abs(j - nums_loc_lst[idx][2]))
    
    find_min(cnt, idx + 1, loc_tuple, val)


N = int(input())
grid = [list(input().strip()) for _ in range(N)]
nums = set(map(str, [i for i in range(1, 10)]))
start_end = set(['S', 'E'])
nums_loc_lst = []
start_end_loc_lst = []

for i in range(N):
    for j in range(N):
        if grid[i][j] in nums:
            nums_loc_lst.append((int(grid[i][j]), i, j))
        elif grid[i][j] in start_end:
            start_end_loc_lst.append((grid[i][j], (i, j)))

if len(nums_loc_lst) < 3:
    print(-1)

else:
    nums_loc_lst.sort()
    start_end_loc_lst.sort(reverse=True)  # S 다음 E로 정렬

    min_val = 200
    find_min(0, 0, start_end_loc_lst[0][1], 0)
    print(min_val)