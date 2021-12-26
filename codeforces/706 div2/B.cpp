#include <iostream>
#include <memory.h>
#include <map>

using namespace std;

int main()
{
    int t;
    int n, k, max, mex;
    int num, cnt;

    cin >> t;
    for(; t > 0 ; t--){
        cin >> n >> k;

        //init.
        max = 0;
        mex = 0;
        cnt = n;
        map <int, bool> s;

        for(int i = 0 ; i < n ; i++){
            cin >> num;
            if(num > max)max = num;
            s.insert(pair<int, bool>(num, true));
        }

        for(int i = 0 ; i < k ; i++){
            for(;s.find(mex)!=s.end();mex++){;}
            num = (mex+max+1)/2;
            if(num > max)max = num;
            s.insert(pair<int, bool>(num, true));
        }
        cout << s.size() << "\n";
    }
    return 0;
}
