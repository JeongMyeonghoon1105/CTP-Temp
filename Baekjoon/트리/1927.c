#include <stdio.h>

#define M 100000

typedef struct node {
    int data;
    struct node *link;
} Node;

typedef struct {
    int index;
    Node *head;
} LinkedList;

void init(LinkedList *L) {
    L->index = 0;
    L->head = NULL;
}

int isEmpty(LinkedList *L) {
    return L->index = 0;
}

int isFull(LinkedList *L) {
    return L->index >= M;
}

void insert(LinkedList *L, int e) {
    if (!isFull(L))
        return;
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = e;
    newNode->link = L->head;

    if (isEmpty(L))
        L->head = newNode;
    else {
        Node *p = NULL;
        while (e > newNode->link->data) {
            p = newNode->link;
            newNode->link = newNode->link->link;
        }
        p->link = newNode;
    }

    L->index++;
}

int pop(LinkedList *L) {

}

void print(LinkedList *L) {
    Node *p = L->head;
    for (int i = 0; i < L->index; i++) {
        printf("%d ", p->data);
        p = p->link;
    }
    printf("\n");
}

int main() {
    LinkedList L;
    init(&L);

    int n, x;  scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x)
            insert(&L, x);
        else
            printf("%d", pop(&L));
    }

    return 0;
}