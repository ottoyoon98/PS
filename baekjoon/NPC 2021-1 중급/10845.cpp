#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n, num;
    string inst;
    int queue[10010],front,rear;
    front = rear = 0;
    cin >> n;
    for(int i = 0 ; i < n ; i++){
        cin >> inst;
        if(inst == "push"){
            cin >> num;
            queue[rear++] = num;
        }
        if(inst == "pop"){
            if(front < rear) cout << queue[front++] << endl;
            else cout << "-1" << endl;
        }
        if(inst == "size"){
            cout << rear-front << endl;
        }
        if(inst == "empty"){
            if(front < rear) cout << "0" << endl;
            else cout << "1" << endl;
        }
        if(inst == "front"){
            if(front < rear) cout << queue[front] << endl;
            else cout << "-1" << endl;
        }
        if(inst == "back"){
            if(front < rear) cout << queue[rear-1] << endl;
            else cout << "-1" << endl;
        }
    }
    return 0;
}
