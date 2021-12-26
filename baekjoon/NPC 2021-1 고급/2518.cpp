#include <iostream>
#include <vector>
#include <memory.h>

using namespace std;


int D[110][110][110][4];
int dis(int a,int b,int n)
{
    return (a-b+n)%n < (b-a+n)%n ? (a-b+n)%n : (b-a+n)%n;
}
void init(int n)
{
    for(int i = 0 ; i <= 100 ; i++){
        for(int j = 0 ; j <= 100 ; j++){
            for(int k = 0 ; k <= 100 ; k++){
                for(int l = 0 ; l < 3 ; l++){
                    D[i][j][k][l] = 999999999;
                }
            }
        }
    }
}
int main()
{
    int n, m, t;
    int dish[3][110]={0,};

    cin >> n;

    init(n);

    for(int i = 0 ; i < 3 ; i++){
        cin >> dish[i][0];
        if(i == 0)dish[i][0]++;
        for(int j = 1 ; j <= dish[i][0] ; j++){
            if(i == 0 && j == 1){
                dish[i][1] = 1;
                continue;
            }
            cin >> t;
            t = (t+n-(n/3*i))%n;
            dish[i][j] = t;
        }
    }
    D[1][0][0][0] = 0;
    int position;
    int iter[3];
    int i, j, k, l;
    for(iter[0] = 1 ; iter[0] <= (int)dish[0][0] ; iter[0]++){
        for(iter[1] = 0 ; iter[1] <= (int)dish[1][0] ; iter[1]++){
            for(iter[2] = 0 ; iter[2] <= (int)dish[2][0] ; iter[2]++){
                for(l = 0 ; l < 3 ; l++){
                    position = dish[l][iter[l]];
                    i = iter[0];
                    j = iter[1];
                    k = iter[2];
                    if(D[i][j][k][l] == 999999999)continue;
                    //cout << i << " "<< j << " " << k << " " << l << " : " << D[i][j][k][l] << "\n";
                    //i+1로 갈 경우
                    if(i+1 <= (int)dish[0][0]){
                        if(D[i+1][j][k][0] > D[i][j][k][l] + dis(position, dish[0][i+1], n)) D[i+1][j][k][0] = D[i][j][k][l] + dis(position, dish[0][i+1], n);
                    }
                    //j+1로 갈 경우
                    if(j+1 <= (int)dish[1][0]){
                        if(D[i][j+1][k][1] > D[i][j][k][l] + dis(position, dish[1][j+1], n)) D[i][j+1][k][1] = D[i][j][k][l] + dis(position, dish[1][j+1], n);
                    }
                    //k+1로 갈 경우
                    if(k+1 <= (int)dish[2][0]){
                        if(D[i][j][k+1][2] > D[i][j][k][l] + dis(position, dish[2][k+1], n)) D[i][j][k+1][2] = D[i][j][k][l] + dis(position, dish[2][k+1], n);
                    }
                }
            }
        }
    }
    int min = 999999999;
    for(int i = 0 ; i < 3 ; i++){
        if(min > D[dish[0][0]][dish[1][0]][dish[2][0]][i])min = D[dish[0][0]][dish[1][0]][dish[2][0]][i];
    }
    cout << min;
    return 0;
}
