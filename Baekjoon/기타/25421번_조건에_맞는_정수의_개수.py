amount = [0, 9]
exclude_bot = [
  [],
  [0, 0, 2], [0, 0, 1],
  [0, 0, 0, 2],
  [0, 0, 0, 1],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 2],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 2]
]
exclude_top = [
  [],
  [0, 0, 0, 0, 0, 0, 2],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 2],
  [0, 0, 0, 0, 1],
  [0, 0, 0, 0, 2],
  [0, 0, 0, 1],
  [0, 0, 0, 2],
  [0, 0, 1], [0, 0, 2]
]

def add_exclude(n):
  for i in range(1, len(exclude_bot)):
    index = len(exclude_bot[i])-1
    while (len(exclude_bot[i]) < n+1):
      exclude_bot[i].append(exclude_bot[i][index] + 2)
      index += 1
  for i in range(1, len(exclude_top)):
    index = len(exclude_top[i])-1
    while (len(exclude_top[i]) < n+1):
      exclude_top[i].append(exclude_top[i][index] + 2)
      index += 1

def dp(n):
  if n == 1:
    return
  for i in range(2, n+1):
    s = 0
    for j in range(1, len(exclude_bot)):
      s += exclude_bot[j][i] + exclude_top[j][i]
    print('s : ', s)
    amount.append((amount[i-1] * 5 - s) % 987654321)

n = int(input())
add_exclude(n)
print(exclude_bot)
print()
print(exclude_top)

dp(n)
print(amount)
print(amount[-1])

# |Ai - Ai+1| ≤ 2 만족하는 경우의 수 다 구하고
# 각 자리가 0 이하 or 10 이상 되는 경우 제외
