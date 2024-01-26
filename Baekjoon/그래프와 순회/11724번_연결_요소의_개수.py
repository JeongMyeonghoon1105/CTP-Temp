# # n, m = map(int, input().split())

# # graph = [[] for i in range(n+1)]
# # visited = [True] + [False for i in range(n)]
# # unvisited = [i for i in range(1, n+1)]
# # # queue = []
# # cc = 0

# # def dfs(v):
# #   visited[v] = True
# #   for i in range(len(graph[v])):
# #     if not visited[graph[v][i]]:
# #       dfs(graph[v][i])

# # # def bfs(v):
# # #   queue.append(v)
# # #   while queue:
# # #     vertex = queue.pop(0)
# # #     # print(vertex, end=' ')
# # #     visited[vertex] = True
# # #     unvisited.remove(vertex)
# # #     for i in range(len(graph[vertex])):
# # #       if not visited[graph[vertex][i]] and graph[vertex][i] not in queue:
# # #         queue.append(graph[vertex][i])


# # for i in range(m):
# #   u, v = map(int, input().split())
# #   graph[u].append(v)
# #   graph[v].append(u)

# # while False in visited:
# #   # print(visited)
# #   for i in range(1, len(visited)):
# #     if not visited[i]:
# #       dfs(i)
# #       cc += 1

# # # while unvisited:
# # #   bfs(unvisited[0])
# # #   cc += 1

# # print(cc)

def dfs(graph, visited, require, start):
  visited.append(start)
  require.remove(start)
  for i in range(len(graph[start])):
    if graph[start][i] not in visited:
      visited, require = dfs(graph, visited, require, graph[start][i])
  return visited, require

def bfs(graph, visited, require, start):
  queue = [start]
  while queue:
    vertex = queue.pop(0)
    visited.append(vertex)
    require.remove(start)
    for i in range(len(graph[vertex])):
      if graph[vertex][i] not in visited and graph[vertex][i] not in queue:
        queue.append(graph[vertex][i])

vertices, edges = map(int, input().split())
graph = [[] for i in range(vertices+1)]
visited = []
require = [i for i in range(1, vertices+1)]
count = 0

for i in range(edges):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

while require:
  visited, require = dfs(graph, visited, require, require[0])
  count += 1

print(count)

# n, m = map(int, input().split())
# connected = [False]

# for i in range(m):
#   u, v = map(int, input().split())
#   u_connect = False
#   v_connect = False

#   if len(connected) == 1:
#     connected.append([u, v])

#   for i in range(1, len(connected)):
#     if u in connected[i]:
#       u_connect = i
#     if v in connected[i]:
#       v_connect = i
#     if u_connect and v_connect:
#       break
  
#   if not u_connect and not v_connect:
#     connected.append([u, v])
#   elif u_connect == v_connect:
#     pass
#   elif not u_connect:
#     connected[v_connect].append(u)
#   elif not v_connect:
#     connected[u_connect].append(v)
#   else:
#     connected[u_connect] += connected[v_connect]
#     connected.pop(v_connect)

# print(len(connected)-1)
