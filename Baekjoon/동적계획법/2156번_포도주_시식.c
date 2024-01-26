#include <stdio.h>

int n = 0, max = 0;
void sumup(int * s, int i, int m, int c);

int main() {
  scanf("%d", &n);
  int * s = (int*)malloc(sizeof(int)*(n+1));
  s[0] = 0;

  for (int i = 1; i <= n; i++)
    scanf("%d", &s[i]);

  sumup(s, 0, 0, 0);
  printf("%d\n", max);
}

void sumup(int * s, int i, int m, int c) {
  m += s[i];

  if (i == n-1 && c <= 0)
    m += s[n];
  if (i >= n-1) {
    // printf("m : %d\n", m);
    if (max < m)
      max = m;
    return;
  }

  if (i == 0) {
    sumup(s, i+1, m, 0);
    sumup(s, i+2, m, 0);
  } else {
    if (c < 1)
      sumup(s, i+1, m, c+1);
    sumup(s, i+2, m, 0);
  }
}
