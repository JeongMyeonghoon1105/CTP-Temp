n, m, r = map(int, input().split())

adjMat = [False] + [[] for i in range(n)]
visited = [False for i in range(n+1)]

def dfs(node):
  if visited[node]:
    return
  visited[node] = True
  print(node)
  for i in adjMat[node]:
    if not visited[i]:
      dfs(i)

for i in range(m):
  u, v = map(int, input().split())
  adjMat[u].append(v)
  adjMat[v].append(u)

for i in range(1, n):
  adjMat[i].sort()

dfs(1)
for i in range(1, len(visited)):
  if not visited[i]:
    print(0)
