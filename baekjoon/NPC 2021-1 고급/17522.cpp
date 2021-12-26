#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct data
{
    int x, y;
}coordinate;
bool compX(const coordinate &A, const coordinate &B)
{
    if(A.x < B.x)return true;
    else if(A.x == B.x && A.y < B.y)return true;
    return 0;
}
int main()
{
    int n;
    cin >> n;
    vector <coordinate> coor;
    coordinate A;
    for(int i = 0 ; i < n ; i++){
        cin >> A.x >> A.y;
        coor.push_back(A);
    }
    sort(coor.begin(), coor.end(), compX);

    for(int i = 0 ; i < n ; i++){
        cout << coor[i].x << " " << coor[i].y << "\n";
    }
    return 0;
}
