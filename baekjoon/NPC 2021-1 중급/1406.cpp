#include <iostream>
#include <list>
#include <string>

using namespace std;

int main()
{
    int m;
    list <char> lt;
    list <char>::iterator iter, iter2;
    string init_str;
    char inst, character;

    cin >> init_str;
    for(int i = 0 ; i < init_str.length() ; i++){
        lt.push_back(init_str[i]);
    }
    iter = lt.end();
    cin >> m;
    for(int i = 0 ; i < m ; i++){
        cin >> inst;
        if(inst == 'P'){
            cin >> character;
            iter=lt.insert(iter, character);
            iter++;
        }
        else if(inst == 'L'){
            if(iter != lt.begin())iter--;
        }
        else if(inst == 'D'){
            if(iter != lt.end())iter++;
        }
        else if(inst == 'B'){
            if(iter != lt.begin())iter = lt.erase(--iter);
        }

    }
    for(iter = lt.begin() ; iter != lt.end() ; iter++){
        cout << *iter;
    }
    return 0;
}
