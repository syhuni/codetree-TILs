k, n = map(int, input().split())

def pick(lst, k, n, cnt):
    if cnt == n:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(1, k + 1):
        lst.append(i)
        pick(lst, k, n, cnt + 1)
        lst.pop()
    
pick([], k, n, 0)