#include <stdio.h>

#define true 1
#define false 0

int main() {
  int a, b, c;   scanf("%d %d %d", &a, &b, &c);
  int power = a, count = 0;
  int save[b];

  while (true) {
    power = (power * a) % c;
    save[count] = power;

    printf("%d\n", power);

    if (power == a % c || power == (a * a) % c) {
      printf("%d\n", save[b % count]);
      break;
    }

    count++;
  }

  return 0;
}


/*
#include <stdio.h>

unsigned int power(unsigned int a, unsigned int b, unsigned int c) {
  if (b == 1)
    return a % c;
  else if (b == 0)
    return 1;
  unsigned int result = 1;
  if (b % 2 == 1)
    result *= (a % c);
  result = (result * (power(a, b / 2, c) * power(a, b / 2, c))) % c;
  return result;
}

int main() {
  unsigned int a, b, c, result;  scanf("%u %u %u", &a, &b, &c);
  result = power(a, b, c);
  printf("%u\n", result);
  return 0;
}
*/

/*
#include <stdio.h>

unsigned int *memo;

void power(unsigned int a, unsigned int b, unsigned int c) {
  if (b == 0)
    return;
  memo[b] = (a % memo[b-1]) % c;
  power(a, b-1, c);
}

int main() {
  unsigned int a, b, c;  scanf("%u %u %u", &a, &b, &c);

  memo = (unsigned int*)malloc(sizeof(unsigned int)*(b+1));
  power(a, b, c);
  printf("%u\n", memo[1]);

  return 0;
}
*/
