n = int(input())

dp = [0] * (n + 1)
dp[2] = 2
dp[3] = 3

if n >= 4:
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp [i - 2]) % 10007
    
print(dp[n])