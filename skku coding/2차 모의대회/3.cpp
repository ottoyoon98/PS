#include <stdio.h>
int main()
{
    int n,k;
    int A1,A2;
    int B1,B2;
    scanf("%d%d",&n,&k);
    scanf("%d%d",&A1,&A2);
    scanf("%d%d",&B1,&B2);
    int cat[3][110];
    for(int i = 1 ; i <= n ; i++)cat[0][i]=i;
    for(int i = 1 ; i <= n ; i++){
        if(A1 <= i && i <= A2)cat[1][i]=cat[0][A2-(i-A1)];
        else cat[1][i]=cat[0][i];
    }
    int temp[110];
    for(int j = 1 ; j <= 2 ; j++){
        for(int i = 1 ; i <= n ; i++){
            if(A1 <= i && i <= A2)temp[i]=cat[j-1][A2-(i-A1)];
            else temp[i]=cat[j-1][i];
        }
        for(int i = 1 ; i <= n ; i++){
            if(B1 <= i && i <= B2)cat[j][i]=temp[B2-(i-B1)];
            else cat[j][i]=temp[i];
        }
    }
    for(int i = 1 ; i <= n ; i++){
        printf("%d\n",cat[k%3][i]);
    }
    return 0;
}
