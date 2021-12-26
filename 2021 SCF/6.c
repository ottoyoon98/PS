#include <stdio.h>
int maxV(int a,int b)
{
	return a>b?a:b;
}
int main() {
	int n,m;
	int map[10010][110]={0,};
	scanf("%d %d",&n,&m);
	for(int i = 1 ; i <= m ; i++){
		for(int j = 1 ; j <= n ; j++){
			scanf("%d",&map[i][j]);
			map[i][j] = maxV(map[i-1][j],map[i][j-1])+map[i][j];
		}
	}
	printf("%d",map[m][n]);
	return 0;
}
