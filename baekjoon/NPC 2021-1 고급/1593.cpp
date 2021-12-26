#include <iostream>
#include <string>
using namespace std;
bool check_str(int *A, int *B)
{
    bool check;
    check = true;
    for(int i = 0 ; i < 52 ; i++){
        if(A[i] != B[i]){
            check = false;
            break;
        }
    }
    return check;
}
int main()
{
    int alpha[60]={0,}, alphaW[60]={0,};
    int g, len, cnt = 0;
    string W, S;
    cin >> g >> len;
    cin >> W >> S;
    for(int i = 0 ; i < g ; i++){
        if(W[i] <= 'Z')alphaW[W[i]-'A']++;
        else alphaW[W[i]-'a'+26]++;
    }
    for(int i = 0 ; i < len ; i++){
        if(i-g >= 0){
            if(S[i-g] <= 'Z')alpha[S[i-g]-'A']--;
            else alpha[S[i-g]-'a'+26]--;
        }
        if(S[i] <= 'Z')alpha[S[i]-'A']++;
        else alpha[S[i]-'a'+26]++;

        if(i >= (g-1)){
            if(check_str(alpha, alphaW)){
                cnt++;
            }
        }
    }
    cout << cnt;
    return 0;
}
