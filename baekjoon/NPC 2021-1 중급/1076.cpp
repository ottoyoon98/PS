#include <iostream>
#include <string>
#include <map>
using namespace std;
int main()
{
    map <string,int> ohm;
    long long R;
    ohm["black"] = 0;
    ohm["brown"] = 1;
    ohm["red"] = 2;
    ohm["orange"] = 3;
    ohm["yellow"] = 4;
    ohm["green"] = 5;
    ohm["blue"] = 6;
    ohm["violet"] = 7;
    ohm["grey"] = 8;
    ohm["white"] = 9;
    string A, B, C;
    cin >> A >> B >> C;
    R = ohm[A]*10+ohm[B];
    for(int i = 0 ; i < ohm[C] ; i++){
        R*=10;
    }
    cout << R;
    return 0;
}
