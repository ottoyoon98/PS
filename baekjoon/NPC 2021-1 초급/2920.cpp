#include <iostream>
using namespace std;
int main()
{
    int scale[8];
    for(int i = 0 ; i < 8 ; i++){
        cin >> scale[i];
    }

    int state;
    if(scale[0] < scale[1])state = 1;
    else state = 0;

    for(int i = 2 ; i < 8 ; i++){
        if(scale[i] > scale[i-1] && state == 0){
            state = 2;
            break;
        }
        else if(scale[i] < scale[i-1] && state == 1){
            state = 2;
            break;
        }
    }
    if(state == 0)cout << "descending";
    else if(state == 1)cout << "ascending";
    else cout << "mixed";
    return 0;
}
