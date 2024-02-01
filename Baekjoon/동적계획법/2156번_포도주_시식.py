def dp(memo, lst, n):
  if n <= 2:
    return sum(lst[:n+1])
  
  m = 0
  
  i = 2
  while i <= n:
    if lst[i] == 0:
      memo[i] = memo[i-1]
    elif i <= 3:
      memo[i] = max(lst[i-2] + lst[i], lst[i-1] + lst[i])
    else:
      memo[i] = max(memo[i-2] + lst[i], memo[i-3] + lst[i-1] + lst[i], memo[i-4] + lst[i-1] + lst[i])
    if memo[i] > m:
      m = memo[i]
    i += 1
  
  return m

n = int(input())
lst = [0] + [int(input()) for i in range(n)]
memo = [0, lst[1]] + [0 for i in range(n-1)]

print(dp(memo, lst, n))
