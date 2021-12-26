#include <iostream>
#include <memory.h>
using namespace std;

int main()
{
    short index[27];
    char word[101];
    int len;
    memset(index, -1, sizeof(index));
    cin >> word;
    len = strlen(word);
    for(int i = 0 ; i < len ; i++){
        if(index[word[i]-'a'] == -1)index[word[i]-'a'] = i;
    }
    for(int i = 0 ; i < 26 ; i++){
        cout << index[i] << " ";
    }
    return 0;
}
