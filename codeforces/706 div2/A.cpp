#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int t;
    int n, k;
    string s;
    bool check;
    cin >> t;
    for(; t > 0 ; t--){
        cin >> n >> k;
        cin >> s;
        check = true;
        if(k*2+1 > n)check = false;
        if(check){
            for(int i = 0 ; i < k ; i++){
                if(s[i] != s[n-1-i]){
                    check = false;
                    break;
                }
            }
        }
        if(check)cout << "YES\n";
        else cout <<"NO\n";
    }
    return 0;
}
