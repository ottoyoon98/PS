#include <stdio.h>
using namespace std;
int main()
{
    long long n,p;
    scanf("%I64d%I64d",&n,&p);
    long long answer = 1;
    for(long long i = 1 ; i <= n ; i++){
        answer = (answer * (i%p))%p;
    }
    printf("%I64d",answer);
    return 0;
}
