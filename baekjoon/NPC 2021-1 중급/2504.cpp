#include <iostream>
#include <string>
using namespace std;
int main()
{
    string bracket;
    cin >> bracket;
    int stack[40], top, empty;
    bool check;
    top = -1;
    check = false;
    for(int i = 0 ; i < bracket.length() ; i++){
        if(bracket[i]=='('){
            stack[++top] = -2;
            continue;
        }
        else if(bracket[i]=='['){
            stack[++top] = -3;
            continue;
        }
        else if(bracket[i]==')'){
            if(top >= 0 && stack[top]==-2)stack[top]=2;
            else if(top > 0 && stack[top-1]==-2){
                empty = stack[top--];
                stack[top] = empty*stack[top]*(-1);
            }
            else
            {
                check = true;
                break;
            }
        }
        else if(bracket[i]==']'){
            if(top >= 0 && stack[top]==-3)stack[top]=3;
            else if(top > 0 && stack[top-1]==-3){
                empty = stack[top--];
                stack[top] = empty*stack[top]*(-1);
            }
            else
            {
                check = true;
                break;
            }
        }
        else
        {
            check = true;
            break;

        }
        if(top > 0 && stack[top] > 0 && stack[top-1] > 0){
            empty = stack[top--];
            stack[top] = empty+stack[top];
        }
    }
    if(top!=0) check = true;
    if(stack[top] < 0)check = true;
    if(check) cout << "0";
    else cout << stack[top];
    return 0;
}
