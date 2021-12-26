#include <iostream>
using namespace std;
int main()
{
    int H, M;
    cin >> H >> M;
    if(M >= 45){
        M -= 45;
    }
    else
    {
        H = (H+24-1)%24;
        M = (M+60)-45;
    }
    cout << H << " " << M;
    return 0;
}
