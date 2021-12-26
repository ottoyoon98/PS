#include <iostream>
#include <map>
#include <string>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    string name, state;
    map<string, string > employee;
    map<string, string>::reverse_iterator iter;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> name >> state;
        if(state == "leave"){
            employee.erase(name);
        }
        else employee[name] = state;
    }
    for(iter = employee.rbegin() ; iter != employee.rend() ; iter++){
        if(iter->second == "enter")cout << iter->first << "\n";
    }
    return 0;
}
