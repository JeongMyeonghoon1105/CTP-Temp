#include <stdio.h>

int blue = 0, white = 0;

void cut(int **p, int r, int c, int len) {\
  if (len == 1) {
    if (p[r][c] == 0)
      blue++;
    else
      white++;
    return;
  }

  int color = p[r][c];

  for (int i = r; i < r + len; i++) {
    for (int j = c; j < c + len; j++) {
      if (p[i][j] != color) {
        cut(p, r, c, len / 2);  cut(p, r + len / 2, c, len / 2);
        cut(p, r, c + len / 2, len / 2);  cut(p, r + len / 2, c + len / 2, len / 2);
        return;
      }
    }
  }

  if (p[r][c] == 0)
    blue++;
  else
    white++;
  return;
}

int main() {
  int n;  scanf("%d", &n);
  int **paper = (int**)malloc(sizeof(int*)*n);
  for (int i = 0; i < n; i++)
    paper[i] = (int*)malloc(sizeof(int)*n);

  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      scanf("%d", &paper[i][j]);
  
  cut(paper, 0, 0, n);

  printf("%d\n%d\n", blue, white);
  return 0;
}
