'''
같은 크기의 2차원 배열을 만들어서 폭탄 1,2,3 놓는 모든 경우를 해보며 비교
폭발 지역을 지우는 것도 고려하니까 헷갈린다
'''
import sys
input = sys.stdin.readline

didj_dict = {
    1: [(-2,0), (-1,0), (1,0), (2,0), (0,0)],
    2: [(1,0), (0,-1), (-1,0), (0,1), (0,0)],
    3: [(1,1), (1,-1), (-1,-1), (-1,1), (0,0)]
}


# 폭발 위치 수 계산하는 함수
def bomb(bomb_lst):
    bomb_cnt = 0
    bomb_grid = [[0] * n for _ in range(n)]
    for idx, ij in enumerate(loc_lst):
        i, j = ij
        for di, dj in didj_dict.get(bomb_lst[idx]):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and bomb_grid[ni][nj] == 0:
                bomb_grid[ni][nj] = 1
                bomb_cnt += 1
    return bomb_cnt


# 폭탄 놓을 위치 수를 세고 위치를 저장 하는 함수
def loc_counter(n, data):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                loc_lst.append((i, j))
    return cnt


# 순열 만들며 개수 비교하는 함수
def dfs(lst):
    global max_val
    if len(loc_lst) == len(lst):
        max_val = max(max_val, bomb(lst))
        return

    for i in range(1, 4):
        lst.append(i)
        dfs(lst)
        lst.pop()

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
loc_lst = []  # 설치 위치 저장 리스트
loc_cnt = loc_counter(n, grid)
max_val = 0
dfs([])
print(max_val)