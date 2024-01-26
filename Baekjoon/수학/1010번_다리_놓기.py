import time

# start = time.time()

memo = [0, 1]
t = int(input())

def factorial(n):
  l = len(memo)
  if n < l:
    return memo[n]
  for i in range(l, n+1):
    memo.append(memo[i-1] * i)
  return memo[-1]

def combination(n, m):
  if m == 0:
    return 1
  elif n == m:
    return 1
  elif m == 1:
    return n
  return factorial(n) // (factorial(n-m) * factorial(m))

for i in range(t):
  r, n = map(int, input().split())
  print(combination(n, r))

# end = time.time()
# print(end - start)
