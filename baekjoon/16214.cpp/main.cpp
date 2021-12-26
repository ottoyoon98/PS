#include <stdio.h>
using namespace std;

int main()
{
    int T;
    long long n,m;
    long long H,pre;
    scanf("%d",&T);
    for(; T > 0 ; T--){
        scanf("%lld %lld", &n, &m);
        pre = -1;
        H = n;
        for(;;){
            pre = H;
            H = 1;
            for(int i = 0 ; i < pre ; i++){
                H = (H*n)%m;
            }
            if(pre == H){
                break;
            }
        }
        printf("%lld\n\n", H);
    }
    return 0;
}
