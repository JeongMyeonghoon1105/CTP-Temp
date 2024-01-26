n = int(input())
memo = [-1001 for i in range(n+1)]

def dp(i):
  while (i <= n):
    if i == 1:
      memo[i] = lst[i]
    else:
      memo[i] = max(memo[i-1]+lst[i], lst[i])
    i += 1

lst = [-1001] + list(map(int, input().split()))
dp(1)
print(max(memo))
