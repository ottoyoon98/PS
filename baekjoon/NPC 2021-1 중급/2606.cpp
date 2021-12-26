#include <iostream>
using namespace std;
int n, m, cnt;
bool matrix[110][110]={0,}, visit[110]={0,};
int dfs(int h)
{
    visit[h] = true;
    cnt++;
    for(int i = 1 ; i <= n ; i++){
        if(!visit[i] && matrix[h][i]){
            dfs(i);
        }
    }
    return 0;
}
int main()
{
    cin >> n >> m;
    int com1, com2;
    for(int i = 0 ; i < m ; i++){
        cin >> com1 >> com2;
        matrix[com1][com2] = matrix[com2][com1] = true;
    }
    dfs(1);
    cout << cnt-1;
    return 0;
}
