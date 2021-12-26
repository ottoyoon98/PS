#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n;
    string ps;
    cin >> n;
    int cnt;
    for(int i = 0 ; i < n ; i++){
        cin >> ps;
        cnt = 0;
        for(int j = 0 ; j < ps.length() ; j++){
            if(ps[j] == '('){
                cnt++;
            }
            else if(ps[j] == ')'){
                cnt--;
                if(cnt < 0)break;
            }
        }
        if(cnt == 0)cout << "YES"<<endl;
        else cout << "NO" <<endl;
    }
    return 0;
}
