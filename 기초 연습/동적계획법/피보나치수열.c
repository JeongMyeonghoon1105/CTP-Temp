#include <stdio.h>

#define LIMIT 100000

unsigned long long int memo[LIMIT] = {0, 1};

unsigned long long int f(int n) {
    if (n <= 1)
        return n;
    if (n > LIMIT) {
        fprintf(stderr, "Out of range.\n");
        return 0;
    }
    for (int i = 2; i <= n; i++)
        memo[i] = memo[i-1] + memo[i-2];
    return memo[n];
}

int main() {
    int n;  scanf("%d", &n);
    printf("%llu", f(n));
    return 0;
}
