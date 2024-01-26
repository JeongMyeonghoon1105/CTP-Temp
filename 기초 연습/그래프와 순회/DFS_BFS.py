def printGraph(graph):
  for i in range(1, len(graph)):
    print(graph[i])

def dfs(graph, visited, start):
  print(start, end=' ')
  visited.append(start)
  for i in range(len(graph[start])):
    if graph[start][i] not in visited:
      visited = dfs(graph, visited, graph[start][i])
  return visited

def bfs(graph, visited, start):
  queue = [start]
  while queue:
    vertex = queue.pop(0)
    print(vertex, end=' ')
    visited.append(vertex)
    for i in range(len(graph[vertex])):
      if graph[vertex][i] not in visited and graph[vertex][i] not in queue:
        queue.append(graph[vertex][i])


vertices, edges, start = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = []

for i in range(edges):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

for i in range(1, vertices+1):
  graph[i].sort()

# DFS
dfs(graph, visited, start)

# Reset
visited = []
print()

# BFS
bfs(graph, visited, start)
