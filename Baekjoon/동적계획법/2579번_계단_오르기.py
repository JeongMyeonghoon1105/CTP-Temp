n = int(input())
points = [0]
memo = [0 for i in range(n+1)]

def dp(i):
  if i > n:
    return
  elif i <= 1:
    memo[i] = points[i]
  elif i == 2:
    memo[2] = points[2] + points[1]
  elif i == 3:
    memo[3] = max(points[2], points[1]) + points[3]
  else:
    memo[i] = max(memo[i-2], points[i-1]+memo[i-3]) + points[i]
  dp(i+1)

for i in range(1, n+1):
  points.append(int(input()))

dp(1)
print(memo[n])
