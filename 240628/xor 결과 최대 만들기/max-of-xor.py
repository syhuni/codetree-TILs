def find_max(cnt, i, val):
    global max_val
    if cnt == m:
        max_val = max(max_val, val)
        return

    if i == n:
        return

    find_max(cnt + 1, i + 1, val ^ nums[i])  # 현재 인덱스 숫자 선택

    find_max(cnt, i + 1, val)  # 현재 인덱스 숫자 선택 x


n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_val = 0
find_max(0, 0, 0)
print(max_val)