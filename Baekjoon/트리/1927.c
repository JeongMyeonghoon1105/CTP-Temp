#include <stdio.h>
#include <stdlib.h>

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
    return L->index == 0;
}

int isFull(LinkedList *L) {
    return L->index >= M;
}

void insert(LinkedList *L, int e) {
    if (isFull(L))
        return;
    
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = e;
    newNode->link = NULL;

    if (isEmpty(L))
        L->head = newNode;
    else if (e < L->head->data) {
        newNode->link = L->head;
        L->head = newNode;
    } else {
        Node *p = L->head;
        while (p->link != NULL && e > p->link->data)
            p = p->link;
        newNode->link = p->link;
        p->link = newNode;
    }

    L->index++;
}

int pop(LinkedList *L) {
    if (isEmpty(L))
        return 0;
    int e = L->head->data;
    // Node *p = L->head;
    L->head = L->head->link;
    L->index--;
    // free(p);
    return e;
}

void print(LinkedList *L) {
    printf("Linked List: ");
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
            printf("%d\n", pop(&L));
        // print(&L);
    }

    return 0;
}
