#include <iostream>
using namespace std;
int main()
{
    int number[10];
    for(int i = 0 ; i < 10 ; i++){
        cin >> number[i];
        number[i] %= 42;
    }
    for(int i = 0 ; i < 10 ; i++){
        for(int j = i+1 ; j < 10 ; j++){
            if(number[i] > number[j])swap(number[i], number[j]);
        }
    }
    int cnt = 1;
    for(int i = 1 ; i < 10 ; i++){
        if(number[i] != number[i-1])cnt++;
    }
    cout << cnt;
    return 0;
}
