#include <iostream>
#include <vector>

using namespace std;

int parent[200100]={0,};
int visit[200100]={0,};

int superParent(int node, int n)
{
    if(visit[node] == n)return -1;
    visit[node] = n;
    if(parent[node] == 0)return node;
    return superParent(parent[node], n);
}
bool comSuperParent(int node1, int node2, int n)
{
    int sp1, sp2;
    sp1 = superParent(node1, n);
    sp2 = superParent(node2, n);
    if(sp2 == -1){
        return true;
    }
    return false;
}
int main()
{
    int N, Q, inst;
    cin >> N >> Q;

    parent[1] = 0;
    for(int i = 2 ; i <= N ; i++){
        cin >> parent[i];
    }
    int node1, node2;
    for(int i = 1 ; i <= N-1+Q ; i++){
        cin >> inst;
        if(inst == 0){
            cin >> node1;
            parent[node1] = 0;
        }
        else if(inst == 1)
        {
            cin >> node1 >> node2;
            if(comSuperParent(node1, node2, i)) cout << "YES\n";
            else cout <<"NO\n";
        }
    }
    return 0;
}
