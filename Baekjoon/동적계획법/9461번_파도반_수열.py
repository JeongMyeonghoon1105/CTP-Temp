memo = [False, 1, 1, 1]

def p(n):
  if n <= 3:
    return 1
  if len(memo) < n:
    memo.append(p(n-1))
  return memo[n-2] + memo[n-3]

t = int(input())
for i in range(t):
  memo = [False, 1, 1, 1]
  n = int(input())
  print(p(n))
