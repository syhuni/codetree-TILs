import sys
input = sys.stdin.readline


def wind(row, direction):
    if direction == 'L':
        temp = building[row][-1]
        for i in range(M - 1, 0, -1):
            building[row][i] = building[row][i - 1]
        building[row][0] = temp
    else:
        temp = building[row][0]
        for i in range(M - 1):
            building[row][i] = building[row][i + 1]
        building[row][-1] = temp


def is_up_prop(row):
    if row == 0:
        return False

    for i in range(M):
        if building[row][i] == building[row - 1][i]:
            return True

    return False


def is_down_prop(row):
    if row == N - 1:
        return False

    for i in range(M):
        if building[row][i] == building[row + 1][i]:
            return True

    return False


N, M, Q = map(int, input().split())  # 행, 열, 바람 수
building = [list(map(int, input().split())) for _ in range(N)]
wind_info = [tuple(input().split()) for _ in range(Q)]

for row, direction in wind_info:
    row = int(row) - 1
    
    wind(row, direction)  # 첫 바람 실행

    # 위쪽 전파
    temp_direction = direction
    for i in range(row, 0, -1):
        if not (is_up_prop(i)):
            break
        
        now_direction = temp_direction
        next_direction = ' '
        if now_direction == 'L':
            next_direction = 'R'
        else:
            next_direction = 'L'
        temp_direction = next_direction
        wind(i - 1, next_direction)

    # 아래쪽 전파
    temp_direction = direction
    for i in range(row, N - 1):
        if not (is_down_prop(i)):
            break
        
        now_direction = temp_direction
        next_direction = ' '
        if now_direction == 'L':
            next_direction = 'R'
        else:
            next_direction = 'L'
        temp_direction = next_direction
        wind(i + 1, next_direction)

for row in building:
    print(' '.join(map(str, row)))