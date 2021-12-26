#include <stdio.h>

using namespace std;

int countStar(int *seg_tree, int k, int l, int r)
{

    return 0;
}
int main()
{
    int n, q, k;
    int a[101000] = {0,};
    int seg_tree[301000] = {0,};
    scanf("%d",&n);
    for(k = 1 ; k <= n ; k*=2);
    printf("%d",k);
    for(int i = 1 ; i <= n ; i++){
        scanf("%d",&a[i]);
        seg_tree[k+i-1] = a[i];
    }
    int instruction, l, r;
    for(int i = 1 ; i < q ; i++){
        scanf("%d", instruction);
        if(instruction == 1){
            scanf("%d %d",&l,&r);
            printf("%d",countStar(*seg_tree, k, l, r));
        }
        else
        {
            scanf("%d",&l);
        }
    }
    return 0;
}
