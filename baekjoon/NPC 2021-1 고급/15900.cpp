#include <iostream>
#include <list>
#include <memory.h>
using namespace std;

int n, cnt;
list <int> edge[500010];
bool visit[500010];

int DFS(int node, int height)
{
    list <int>::iterator iter;
    visit[node] = true;
    if(node != 1 && edge[node].size() == 1){
        cnt += height;
    }
    else
    {
        for(iter = edge[node].begin() ; iter != edge[node].end() ; iter++){
            if(visit[*iter])continue;
            DFS(*iter, height+1);
        }
    }
    return 0;
}
int main()
{

    cin >> n;
    int node1, node2;
    memset(visit, false, n+1);
    for(int i = 0 ; i < n-1 ; i++){
        cin >> node1 >> node2;
        edge[node1].push_back(node2);
        edge[node2].push_back(node1);
    }

    cnt = 0;
    DFS(1,0);
    if(cnt % 2 == 1)cout << "Yes";
    else cout << "No";
    return 0;
}
