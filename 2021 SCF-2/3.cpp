
#include <stdio.h>

int parent[500100]={0,};
int level[500100]={0,};
int find_level(int h)
{
	if(h == 0) return 0;
	if(level[h] == 0){
		level[h] = find_level(parent[h])+1;
	}
	return level[h];
}
int isParent(int s, int e)
{
	while(level[s] < level[e]){
		e = parent[e];
	}
	if(s != e)return 0;
	else return 1;
}
int main() {
	int n, q;
	scanf("%d %d",&n,&q);
	int s,e;
	for(int i = 0 ; i < n-1 ; i++){
		scanf("%d %d",&s, &e);
		parent[e] = s;
	}
	for(int i = 1 ; i <= n ; i++)	find_level(i);

	for(int queryI = 0 ; queryI < q ; queryI++){
		//s가 e의 parent인지 확인하기
		scanf("%d %d",&s, &e);
		if(level[s] >= level[e]){
			printf("no\n");
			continue;
		}
		if(isParent(s, e)) printf("yes\n");
		else printf("no\n");
	}
	return 0;
}
