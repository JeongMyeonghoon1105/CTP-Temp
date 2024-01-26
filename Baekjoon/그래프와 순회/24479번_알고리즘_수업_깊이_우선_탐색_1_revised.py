import sys
sys.setrecursionlimit(10 ** 6)

tree = []
orderList = []
order = 1

def dfs(v):
  # if orderList[v]:
  #   return
  global order
  orderList[v] = order
  order += 1
  for i in range(len(tree[v])):
    if not orderList[tree[v][i]]:
      dfs(tree[v][i])

n, m, r = map(int, input().split())
for i in range(n+1):
  tree.append([])
  orderList.append(0)

for i in range(m):
  v1, v2 = map(int, input().split())
  tree[v1].append(v2)
  tree[v2].append(v1)

for i in range(1, n+1):
  tree[i].sort()

dfs(r)

for i in range(1, n+1):
  print(orderList[i])
