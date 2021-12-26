#include <iostream>

using namespace std;

int main()
{
    int n, m;
    int card[100];
    int max = 0, sum;

    cin >> n >> m;
    for(int i = 0 ; i < n ; i++){
        cin >> card[i];
    }
    for(int i = 0 ; i < n ; i++){
        for(int j = i+1 ; j < n ; j++){
            for(int k = j+1 ; k < n ;k++){
                sum = card[i]+card[j]+card[k];
                if(max < sum && sum <= m){
                    max = sum;
                }
            }
        }
    }
    cout << max;
    return 0;
}
