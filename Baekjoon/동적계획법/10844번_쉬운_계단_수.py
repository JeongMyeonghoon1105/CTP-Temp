n = int(input())
memo = [0 for i in range(n+1)]

def dp(i):
  while i <= n:
    if i == 1:
      memo[i] = 9
    else:
      memo[i] = (memo[i-1] * 2 - (i-1)) % 1000000000
    i += 1

dp(1)
print(memo[n])
