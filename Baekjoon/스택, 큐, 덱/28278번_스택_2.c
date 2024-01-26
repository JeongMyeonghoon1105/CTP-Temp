#include <stdio.h>

#define M 1000000

typedef struct st {
    int head;
    int stack[M];
} StackType;

void init(StackType *S) {
    S->head = 0;
}

int isEmpty(StackType *S) {
    return S->head == 0;
}

int isFull(StackType *S) {
    return S->head >= M;
}

void push(StackType *S, int x) {
    if (isFull(S))
        return;
    S->stack[S->head] = x;
    S->head++;
}

int pop(StackType *S) {
    if (isEmpty(S))
        return -1;
    int data = S->stack[S->head];
    S->head--;
    return data;
}

int main() {
    printf("hello\n");
    StackType S;
    init(&S);

    int n;  scanf("%d", &n);
    int command = 0, x = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &command);

        switch (command) {
            case 1:
                scanf("%d", &x);
                push(&S, x);
                break;
            case 2:
                printf("%d\n", pop(&S));
            case 3:
                printf("%d\n", S.head);
            case 4:
                (isEmpty(&S)) ? printf("1\n") : printf("0\n");
            case 5:
                (isEmpty(&S)) ? printf("-1\n") : printf("%d\n", S.stack[S.head]);
            default:
                break;
        }
    }

    return 0;
}
