'''
같은 크기의 2차원 배열을 만들어서 폭탄 1,2,3 놓는 모든 경우를 해보며 비교
폭발 지역을 지우는 것도 고려하니까 헷갈린다
'''
import sys
input = sys.stdin.readline

didj_dict = {
    1: [(-2,0), (-1,0), (1,0), (2,0)],
    2: [(1,0), (0,-1), (-1,0), (0,1)],
    3: [(1,1), (1,-1), (-1,-1), (-1,1)]
}


def bomb(def_cnt):
    global loc_cnt
    global max_val
    global bomb_cnt
    if def_cnt == loc_cnt:
        max_val = max(max_val, bomb_cnt)
        return

    for k in range(1, 4):  # 폭탄 종류 1~3
        for i, j in loc_lst:
            # 폭발 구역 체크
            bomb_grid[i][j] += 1
            if bomb_grid[i][j] == 1:
                bomb_cnt += 1
            for di, dj in didj_dict.get(k):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    bomb_grid[ni][nj] += 1
                    if bomb_grid[ni][nj] == 1:
                        bomb_cnt += 1
            # 함수 실행
            bomb(def_cnt + 1)
            # 폭발 구역 원복
            bomb_grid[i][j] -= 1
            if bomb_grid[i][j] == 0:
                bomb_cnt -= 1
            for di, dj in didj_dict.get(k):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    bomb_grid[ni][nj] -= 1
                    if bomb_grid[ni][nj] == 0:
                        bomb_cnt -= 1


# 폭탄 놓을 위치 수를 세고 위치를 저장 하는 함수
def loc_counter(n, data):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                cnt += 1
                loc_lst.append((i, j))
    return cnt
    

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bomb_grid = [[0] * n for _ in range(n)]
loc_lst = []  # 설치 위치 저장 리스트
loc_cnt = loc_counter(n, grid)
max_val = 0
bomb_cnt = 0
bomb(0)
print(max_val)