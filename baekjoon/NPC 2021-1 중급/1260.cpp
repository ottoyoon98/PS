#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int DFS(int n, int h, bool (*matrix)[1010])
{
    int stack[1010], top=0;
    bool visit[1010] = {0,}, check;
    int P, Pi;
    stack[++top] = h;
    stack[top+1] = 0;
    for(;;){
        if(top <= 0)break;
        P = stack[top];
        Pi = stack[top+1];
        if(Pi == 0){
            visit[P] = true;
            cout << P << " ";
        }
        check = false;
        for(int i = Pi+1 ; i <= n ; i++){
            if(matrix[P][i] && !visit[i]){
                stack[++top] = i;
                stack[top+1] = 0;
                check = true;
                break;
            }
        }
        if(!check){
            top--;
        }
    }
    cout << endl;
    return 0;
}
int BFS(int n, int h, bool (*matrix)[1010])
{
    int queue[2010], front=0,rear=0;
    bool visit[1010] = {0,};
    int P;
    queue[rear++] = h;
    visit[h] = true;
    for(;;){
        if(front>=rear)break;
        P = queue[front++];
        cout << P << " ";
        for(int i = 1 ; i <= n ; i++){
            if(matrix[P][i] && !visit[i]){
                queue[rear++]=i;
                visit[i] = true;
            }
        }
    }
    cout << endl;
    return 0;
}
int main()
{
    int N, M, V, s, e;
    bool matrix[1010][1010]={false,};
    cin >> N >> M >> V;
    for(int i = 0 ; i < M ; i++){
        cin >> s >> e;
        matrix[s][e] = matrix[e][s] = true;
    }
    DFS(N, V, matrix);
    BFS(N, V, matrix);
    return 0;
}
