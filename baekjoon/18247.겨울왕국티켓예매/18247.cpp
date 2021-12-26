#include <stdio.h>

using namespace std;

int main()
{
    int T,N,M;
    scanf("%d ", &T);
    for(int testCase = 1 ; testCase <= T ; testCase++){
        scanf("%d%d",&N,&M);
        if(N < 12 || M < 4){
            printf("-1\n");
            continue;
        }
        printf("%d\n",M*11+4);
    }
    return 0;
}
