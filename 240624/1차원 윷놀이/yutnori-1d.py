def dfs(cnt):
    global max_val
    if max_val == k:
        return

    if cnt == n:
        max_val = max(max_val, play(perm))
        return

    for i in range(1, k + 1):
        perm.append(i)
        dfs(cnt + 1)
        perm.pop()


def play(perm):
    goal = 0
    players = [1] * (k + 1)
    for idx, num in enumerate(perm):
        players[num] += arr[idx]
    for player in players[1:]:
        if player >= m:
            goal += 1
    return goal


n, m, k = map(int, input().split())  # 턴의 수, 판 길이, 말의 수
arr = list(map(int, input().split()))
perm = []
max_val = 0
dfs(0)
print(max_val)