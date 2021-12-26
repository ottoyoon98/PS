#include <stdio.h>
#include <string.h>
using namespace std;
int n,cnt;
int alphabet[26];
char input_word[60];
char word[110][60];
int main()
{
    scanf("%d",&n);
    int index;
    for(int i = 0 ; i < n ; i++){
        scanf("%s",input_word);
        index = 0;
        for(int j = 0 ; j < 26 ; j++)alphabet[j]=-1;
        for(int j = 0 ; j < strlen(input_word) ; j++){
            if(alphabet[input_word[j]-'a']==-1){
                alphabet[input_word[j]-'a']=index++;
            }
            word[i][j] = alphabet[input_word[j]-'a']+'a';
        }
        word[i][strlen(input_word)]='\0';
    }

    for(int i = 0 ; i < n ; i++){
        for(int j = i+1 ; j < n ; j++){
            if(!strcmp(word[i],word[j]))cnt++;
        }
    }
    printf("%d",cnt);
    return 0;
}
