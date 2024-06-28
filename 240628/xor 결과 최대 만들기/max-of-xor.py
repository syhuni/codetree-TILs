def combinate(cnt, k):
    global max_val
    if cnt == m:
        result = comb[0]
        for num in comb[1:]:
            result = result ^ num
        max_val = max(max_val, result)
        return

    for i in range(k, n):
        comb.append(nums[i])
        combinate(cnt + 1, i + 1)
        comb.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_val = 0
comb = []
combinate(0, 0)
print(max_val)