#include <iostream>
using namespace std;
int main()
{
    long long n, m, i, j;
    cin >> n;
    for(i = 1 ;; i++){
        m = (i+1ll)*((1ll<<(i+1))-1)+i;
        if(n <= m){
            cout << i;
            break;
        }
    }
    return 0;
}
