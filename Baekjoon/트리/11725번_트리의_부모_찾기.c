#include <stdio.h>

#define true 1
#define false 0

void initTree(int **adjMat, int n) {
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      adjMat[i][j] = false;
}

void insertEdge(int **adjMat, int v1, int v2) {
  adjMat[v1][v2] = adjMat[v2][v1] = true;
}

void searchParent(int **adjMat, int *parentArr, int i, int n) {
  for (int j = 1; j <= n; j++) {
    if (adjMat[i][j] && !parentArr[j]) {
      parentArr[j] = i;
      searchParent(adjMat, parentArr, j, n);
    }
  }
}

int main() {
  int n, v1, v2;  scanf("%d", &n);
  int **adjMat = (int**)malloc(sizeof(int*)*(n+1));
  for (int i = 0; i < n+1; i++)
    adjMat[i] = (int*)malloc(sizeof(int)*(n+1));
  int parentArr[n+1];
  for (int i = 0; i < n+1; i++)
    parentArr[i] = false;

  initTree(adjMat, n);

  for (int i = 0; i < n-1; i++) {
    scanf("%d %d", &v1, &v2);
    insertEdge(adjMat, v1, v2);
  }

  searchParent(adjMat, parentArr, 1, n);

  for (int i = 2; i <= n; i++)
    printf("%d\n", parentArr[i]);

  return 0;
}
