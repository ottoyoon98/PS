#include <iostream>
using namespace std;
int main()
{
    int n, min;
    cin >> n;
    min = n;
    for(int i = 0 ; i <= n/5 ; i++){
        if((n-(5*i))%3==0){
            if((n-(5*i))/3+i < min) min = (n-(5*i))/3+i;
        }
    }
    if(min == n)cout << "-1";
    else cout << min;
    return 0;
}
