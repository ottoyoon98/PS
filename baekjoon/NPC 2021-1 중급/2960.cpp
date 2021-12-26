#include <iostream>
using namespace std;
int main()
{
    int n, k, cnt;
    bool sieve[1100]={false,};
    cnt = 0;
    cin >> n >> k;
    for(int i = 2 ; i <= n ; i++){
        if(sieve[i])continue;
        for(int j = i ; j <= n ; j=j+i){
            if(!sieve[j]){
                sieve[j] = true;
                cnt++;
                if(cnt == k){
                    cout << j;
                    return 0;
                }
            }
        }
    }
    return 0;
}
