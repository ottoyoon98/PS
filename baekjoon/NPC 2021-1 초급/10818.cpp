#include <iostream>
using namespace std;
int main()
{
    int n, number, max = -1000000, min = 1000000;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> number;
        if(number > max) max = number;
        if(number < min) min = number;
    }
    cout << min << " " << max;
    return 0;
}
