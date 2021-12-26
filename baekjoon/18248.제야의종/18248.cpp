#include <stdio.h>
#include <algorithm>
using namespace std;

typedef struct listen{
    int index, num;
}Listen;

int fo(const Listen &A,const Listen &B)
{
    if(A.num > B.num)return 0;
    return 1;
}
int main()
{
    int N,M;
    int a[1010][110];
    Listen L[1010];
    scanf("%d %d",&N,&M);
    for(int i = 0 ; i < N ; i++){
        L[i].index = i;
        L[i].num = 0;
        for(int j = 0 ; j < M ; j++){
            scanf("%d",&a[i][j]);
            L[i].num += a[i][j];
        }
    }
    sort(L, L+N, fo);
    for(int i = 0 ; i < N-1 ; i++){
        for(int j = 0 ; j < M ; j++){
            if(a[L[i].index][j] > a[L[i+1].index][j]){
                printf("NO");
                return 0;
            }
        }
    }
    printf("YES");
    return 0;
}
