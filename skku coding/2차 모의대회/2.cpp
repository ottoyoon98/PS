#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
struct Judge{
    int len;
    char str[16];
};
bool comp(const Judge &s1, const Judge &s2){
    if(strcmp(s1.str, s2.str)>0) return true;
    else return false;
}
int main()
{
    int n;
    scanf("%d",&n);

    Judge *A = new Judge[n];
    Judge *B = new Judge[n];

    for(int i = 0 ; i < n ; i++){
        scanf("%s",A[i].str);
        A[i].len=strlen(A[i].str);
    }
    for(int i = 0 ; i < n ; i++){
        scanf("%s",B[i].str);
        B[i].len=strlen(B[i].str);
    }
    sort(A,A+n,comp);
    sort(B,B+n,comp);
    int cnt=0,iter1=0,iter2=0;
    while(iter1<n && iter2<n){
        if(strcmp(A[iter1].str,B[iter2].str)==0){
            cnt++;
            iter1++;
            iter2++;
        }
        else if(strcmp(A[iter1].str,B[iter2].str)>0)iter1++;
        else iter2++;
    }
    printf("%d",cnt);
    return 0;
}
