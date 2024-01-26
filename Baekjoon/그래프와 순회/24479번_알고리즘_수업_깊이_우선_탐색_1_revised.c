#include <stdio.h>

#define true 1
#define false 0

int **tree;
int treeLen = 0;

int *visited;
int visitedLen = 0;

int *orderList;
int order = 1;

int isIn(int v) {
  for (int i = 0; i < visitedLen; i++)
    if (visited[i] == v)
      return true;
  return false;
}

void dfs(int v) {
  if (isIn(v))
    return;
  visited[visitedLen] = v;
  visitedLen++;
  orderList[v] = order;
  order++;

  for (int i = 0; i < )
}

/*
def dfs(v):
  if v in visited:
    return
  visited.append(v)
  global order
  orderList[v] = order
  order += 1
  for i in range(len(tree[v])):
    if tree[v][i] not in visited:
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
*/
