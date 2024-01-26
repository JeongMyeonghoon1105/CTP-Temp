#include <stdio.h>

typedef int element;

typedef struct node {
  element data;
  struct node *left, *right;
} node;

typedef struct {
  struct node *root;
} tree;

void initTree(tree *t) {
  t->root = (node*)malloc(sizeof(node));
  t->root->data = -1;
  t->root->left = t->root->right = NULL;
}

void insertNode(element key, tree *t) {
  if (t->root->data == -1){
    
  }
}

int main() {

}