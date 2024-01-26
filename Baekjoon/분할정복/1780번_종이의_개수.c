#include <stdio.h>

int n1 = 0, zero = 0, p1 = 0;

void cut(int **p, int r, int c, int len) {\
  if (len == 1) {
    if (p[r][c] == -1)
      n1++;
    else if (p[r][c] == 0)
      zero++;
    else
      p1++;
    return;
  }

  int num = p[r][c];

  for (int i = r; i < r + len; i++) {
    for (int j = c; j < c + len; j++) {
      if (p[i][j] != num) {
        cut(p, r, c, len / 3);
        cut(p, r + len / 3, c, len / 3);
        cut(p, r + len / 3 * 2, c, len / 3);
        cut(p, r, c + len / 3, len / 3);
        cut(p, r, c + len / 3 * 2, len / 3);
        cut(p, r + len / 3, c + len / 3, len / 3);
        cut(p, r + len / 3 * 2, c + len / 3, len / 3);
        cut(p, r + len / 3, c + len / 3 * 2, len / 3);
        cut(p, r + len / 3 * 2, c + len / 3 * 2, len / 3);
        return;
      }
    }
  }

  if (p[r][c] == -1)
    n1++;
  else if (p[r][c] == 0)
    zero++;
  else
    p1++;
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

  printf("%d\n%d\n%d\n", n1, zero, p1);
  return 0;
}
