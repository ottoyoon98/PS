#include <stdio.h>
#include <stdlib.h>
#define null 0
using namespace std;

typedef struct node{
    int key;
    struct node *parents;
    struct node *left;
    struct node *right;
}Node;
void postorder(struct node *cp)
{
    if(cp->left != null) postorder(cp->left);
    if(cp->right != null) postorder(cp->right);
    printf("%d\n",cp->key);
}
int main()
{
    int key_value;
    Node *head = null, *newNode = null, *cpNode = null;
    for(;;){
        key_value = 0;
        if(scanf("%d",&key_value)==EOF)break;

        newNode = (Node*)malloc(sizeof(Node));
        newNode->key = key_value;
        newNode->parents = newNode->left = newNode->right = null;

        if(head == null){
            head = cpNode = newNode;
            continue;
        }
        else
        {
            if(newNode->key < cpNode->key){
                cpNode->left = newNode;
                newNode->parents = cpNode;
            }
            else{
                while(cpNode->parents != 0 && cpNode->parents->key < newNode->key){
                    cpNode = cpNode->parents;
                }
                while(cpNode->right != 0){
                    cpNode = cpNode->right;
                }
                cpNode->right = newNode;
                newNode->parents = cpNode;
            }
            cpNode = newNode;
        }
    }
    postorder(head);
    return 0;
}
