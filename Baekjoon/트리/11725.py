import sys

n = int(input())
nodes = [False for i in range(n+1)]
edges = []

def search(num):
  for i in range(len(edges)):
    if num == edges[i][0]:
      if nodes[num] != edges[i][1]:
        nodes[edges[i][1]] = num
        search(edges[i][1])
    elif num == edges[i][1]:
      if nodes[num] != edges[i][0]:
        nodes[edges[i][0]] = num
        search(edges[i][0])

for i in range(n-1):
  v1, v2 = map(int, sys.stdin.readline().split())
  edges.append([v1, v2])

search(1)

for i in range(2, n+1):
  print(nodes[i])
