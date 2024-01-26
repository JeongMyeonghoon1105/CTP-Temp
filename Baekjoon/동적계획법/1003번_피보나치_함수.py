memo = [[1, 0], [0, 1]]

def dp(n):
  if n <= 1:
    print(memo[n][0], memo[n][1])
    return
  for i in range(2, n+1):
    memo.append([memo[i-1][0]+memo[i-2][0], memo[i-1][1]+memo[i-2][1]])
    pass

t = int(input())

for i in range(t):
  n = int(input())
  dp(n)
  if n > 1: 
    print(memo[-1][0], memo[-1][1])
  memo = [[1, 0], [0, 1]]