#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    char word[1000001];
    int len;
    int alphabet[26];

    cin >> word;
    len = strlen(word);
    for(int i = 0 ; i < len ; i++){
        if(word[i] <= 'Z')alphabet[word[i]-'A']++;
        else alphabet[word[i]-'a']++;
    }
    int max=-1, maxi=-1;
    for(int i = 0 ; i < 26 ; i++){
        if(max < alphabet[i]){
            max = alphabet[i];
            maxi = i;
        }
        else if(max == alphabet[i]){
            maxi = -1;
        }
    }
    if(maxi == -1)cout << "?";
    else cout << char(maxi+'A');
    return 0;
}
