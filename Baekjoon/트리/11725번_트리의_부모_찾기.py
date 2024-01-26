import sys

adjMat = []
parentArr = []

def insertEdge(adjMat, v1, v2):
  adjMat[v1][v2] = adjMat[v2][v1] = True
  
def searchParent(adjMat, parentArr, start, length):
  for i in range(1, length+1):
    if adjMat[start][i] and not parentArr[i]:
      parentArr[i] = start
      searchParent(adjMat, parentArr, i, n)

n = int(input())
adjMat = [[False for i in range(n+1)] for j in range(n+1)]
parentArr = [False for i in range(n+1)]

for i in range(n-1):
  v1, v2 = map(int, sys.stdin.readline().split())
  insertEdge(adjMat, v1, v2)

searchParent(adjMat, parentArr, 1, n)

for i in range(2, n+1):
  print(parentArr[i])
