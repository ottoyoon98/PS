#include <iostream>

using namespace std;

int main()
{
    int N, X, number, num[10001], cnt=0;
    cin >> N >> X;
    for(int i = 0 ; i < N ; i++){
        cin >> number;
        if(number < X){
            num[cnt++] = number;
        }
    }
    for(int i = 0 ; i < cnt ; i++){
        cout << num[i] << " ";
    }
    return 0;
}
