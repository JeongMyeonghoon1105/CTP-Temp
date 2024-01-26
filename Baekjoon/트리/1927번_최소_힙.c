#include <stdio.h>

#define true 1
#define false 0
#define N 100001

typedef int element;

typedef struct {
    int rear;
    element heap[N];
} HeapType;

void init(HeapType *H) {
    H->rear = 1;
    for (int i = 0; i < N; i++)
        H->heap[i] = -1;
}

int isLeaf(HeapType *H, int index) {
    if (index * 2 >= N)
        return true;
    return H->heap[index * 2] == -1 && H->heap[index * 2 + 1] == -1;
}

void swap(HeapType *H, int a, int b) {
    element temp = H->heap[a];
    H->heap[a] = H->heap[b];
    H->heap[b] = temp;
}

void insert(HeapType *H, element e) {
    H->heap[H->rear] = e;
    int pos = H->rear;
    while (pos >= 1 && H->heap[pos] < H->heap[pos / 2]) {
        swap(H, pos, pos / 2);
        pos /= 2;
    }
    H->rear++;
}

element delete(HeapType *H) {
    if (H->rear == 1)
        return 0;
    int e = H->heap[1];
    H->heap[1] = H->heap[H->rear-1];
    H->heap[H->rear-1] = -1;
    H->rear--;

    int p = 1, lc = p * 2, rc = p * 2 + 1;
    while (((H->heap[p] > H->heap[lc] && H->heap[lc] != -1) || (H->heap[p] > H->heap[rc] && H->heap[rc] != -1)) && !isLeaf(H, p)) {
        lc = p * 2, rc = p * 2 + 1;
        if (H->heap[lc] < H->heap[rc]) {
            swap(H, p, lc);
            p *= 2;
        } else {
            swap(H, p, rc);
            p = p * 2 + 1;
        }
    }

    return e;
}

void print(HeapType *H) {
    for (int i = 1; i < H->rear; i++)
        printf("%d ", H->heap[i]);
    printf("\n");
}

int main() {
    HeapType h;
    init(&h);

    int n, inp;  scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &inp);
        
        if (inp)
            insert(&h, inp);
        else
            printf("%d\n", delete(&h));
        
        // print(&h);
    }
}