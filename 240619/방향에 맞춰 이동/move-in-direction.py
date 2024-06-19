dxdy = {'E': (1,0), 'S': (0,-1), 'W': (-1,0), 'N': (0,1)}
n = int(input())
x, y = 0, 0

for _ in range(n):
    d, cnt = input().split()
    cnt = int(cnt)
    dx, dy = dxdy.get(d)
    x = x + dx * cnt
    y = y + dy * cnt

print(x, end=' ')
print(y)