#include <iostream>
using namespace std;
int main()
{
    int T, n, cnt;
    int A[1010];
    cin >> T;
    for(int i = 0 ; i < T ; i++){
        cin >> n;
        for(int j = 0 ; j < n ; j++){
            cin >> A[j];
        }
        cnt = 0;
        for(int j = 0 ; j < n ; j++){
            for(int k = 0 ; k < n-j-1 ; k++){
                if(A[k] > A[k+1]){
                    swap(A[k], A[k+1]);
                    cnt++;
                }
            }
        }
        cout << cnt << endl;
    }
    return 0;
}
