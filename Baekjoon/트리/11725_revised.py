import sys

parent = []

def search(adjMat, node):
  if visited[node]:
    return
  visited[node] = True
  for i in adjMat[node]:
    if not visited[i]:
      parent[i] = node
    search(adjMat, i)
  
n = int(input())

adjMat = [False] + [[] for i in range(n)]
parent = [False for i in range(n+1)]
visited = [False for i in range(n+1)]

for i in range(n-1):
  n1, n2 = map(int, sys.stdin.readline().split())
  adjMat[n1].append(n2)
  adjMat[n2].append(n1)

search(adjMat, 1)

for i in range(2, len(parent)):
  print(parent[i])
