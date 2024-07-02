import sys
input = sys.stdin.readline

n, t = map(int, input().split())
belt_top = list(map(int, input().split()))
belt_bot = list(map(int, input().split()))

for _  in range(t):
    temp_top = belt_top[-1]
    temp_bot = belt_bot[-1]
    for i in range(n - 1, 0, -1):
        belt_top[i] = belt_top[i - 1]
        belt_bot[i] = belt_bot[i - 1]
    belt_top[0] = temp_bot
    belt_bot[0] = temp_top

print(' '.join(map(str, belt_top)))
print(' '.join(map(str, belt_bot)))