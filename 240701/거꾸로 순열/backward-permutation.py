n = int(input())
perm =[]
visited = [0] * (n + 1)

def dfs(cnt):
    if cnt == n:
        print(' '.join(map(str, perm)))
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        perm.append(i)
        visited[i] = 1

        dfs(cnt + 1)

        perm.pop()
        visited[i] = 0

dfs(0)