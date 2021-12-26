#include <stdio.h>
int main()
{
    int n,w;
    int wi,li;
    int sum=0;
    scanf("%d%d",&w,&n);
    for(int i = 0 ; i < n ; i++){
        scanf("%d %d",&wi,&li);
        sum+=(wi*li);
    }
    printf("%d",sum/w);
    return 0;
}
