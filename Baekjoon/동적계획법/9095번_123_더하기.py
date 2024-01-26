memo = [0, 1, 2, 4]

def dp(n):
  if n < len(memo):
    return
  while len(memo) <= n:
    i = len(memo)
    memo.append(memo[i-3] + memo[i-2] + memo[i-1])
  
t = int(input())
for i in range(t):
  n = int(input())
  dp(n)
  print(memo[n])
