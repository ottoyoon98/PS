#include <stdio.h>
#include <string.h>
#include <ctype.h>
using namespace std;

int main()
{
    char enflag[]="5c6a6a6d7d6665766661605d776d62764c684b4f705d537e566c556052724c62";
    printf("enFlag: %s",enflag);
    printf("\n");
    printf("deFlag: ");

    char empty;
    char num;
    for(int i = 0 ; i < strlen(enflag) ; i++){
        if(isdigit(enflag[i]))empty = enflag[i]-'0';
        else if(isalpha(enflag[i]))empty = enflag[i]-'a'+10;
        if(i%2==1){
            num = num*16+empty;
            num = num^(0x04);
        }
        else{
            num = empty;
        }
        if(i%2==1){
            printf("%c",num);
//            if(empty < 10) printf("%c",empty+'0');
//            else printf("%c",empty-10+'a');
        }
    }
    printf("\n\n");
    return 0;
}


