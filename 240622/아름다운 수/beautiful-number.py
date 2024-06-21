def find_beautiful_num(lst):
    global cnt
    if len(lst) > n:
        return
    
    if len(lst) == n:
        cnt += 1
        return
    
    if n < 4:
        for i in range(1, n + 1):
            for _ in range(i):
                lst.append(i)
            find_beautiful_num(lst)
            for _ in range(i):
                lst.pop()

    else:
        for i in range(1, 5):
            for _ in range(i):
                lst.append(i)
            find_beautiful_num(lst)
            for _ in range(i):
                lst.pop()


n = int(input())
cnt = 0
find_beautiful_num([])
print(cnt)