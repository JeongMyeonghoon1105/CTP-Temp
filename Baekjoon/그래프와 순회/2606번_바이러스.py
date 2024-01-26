v = int(input())
e = int(input())

graph = [[] for i in range(v+1)]
visited = []
count = 0

def printGraph():
  for i in range(1, len(graph)):
    print(graph[i])

def dfs(v):
  visited.append(v)
  global count
  count += 1
  for i in range(len(graph[v])):
    if graph[v][i] not in visited:
      dfs(graph[v][i])

for i in range(e):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

# printGraph()
dfs(1)
print(count-1)
