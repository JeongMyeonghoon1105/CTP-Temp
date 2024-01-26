#include <stdio.h>

int recursive(int digit, int num) {
  if (digit == 1)
    return 1;
  
  if (num == 1)
    return recursive(digit-1, 1) + recursive(digit-1, 2) + recursive(digit-1, 3);
  else if (num == 2)
    return recursive(digit-1, 1) + recursive(digit-1, 2) + recursive(digit-1, 3) + recursive(digit-1, 4);
  else if (num == 8)
    return recursive(digit-1, 6) + recursive(digit-1, 7) + recursive(digit-1, 8) + recursive(digit-1, 9);
  else if (num == 9)
    return recursive(digit-1, 7) + recursive(digit-1, 8) + recursive(digit-1, 9);
  else
    return recursive(digit-1, num-2) + recursive(digit-1, num-1) + recursive(digit-1, num) + recursive(digit-1, num+1) + recursive(digit-1, num+2);
}

int main(void) {
  int n = 0, count = 0;
  scanf("%d", &n);

  for (int i = 1; i <= 9; i++)
    count = count + recursive(n, i);

  printf("%d\n", count % 987654321);
  
  return 0;
}