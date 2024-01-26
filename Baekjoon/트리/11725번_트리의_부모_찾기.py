n = int(input())
parent = [False for i in range(n+1)]
adjMat = [False] + [[] for i in range(1, n+1)]
visited = [False for i in range(n+1)]
visited[1] = True
queue = [1]

for i in range(n-1):
  n1, n2 = map(int, input().split())
  adjMat[n1].append(n2)
  adjMat[n2].append(n1)

while queue:
  node = queue.pop()
  for j in adjMat[node]:
    if not visited[j]:
      queue.append(j)
      visited[j] = True
      parent[j] = node

for i in range(2, n+1):
  print(parent[i])
