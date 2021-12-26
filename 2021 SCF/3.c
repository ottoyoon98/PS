#include <stdio.h>
int main() {
	int n;
	char space[100][100]={0,};
	int space2[100][100]={0,};
	int furniture[100]={0,},cnt = 0;
	scanf("%d",&n);
	for(int i = 1 ; i <= n ; i++){
		scanf("%s",&space[i][1]);
		for(int j = 1 ; j <= n ; j++){
			space2[i][j] = space2[i-1][j] + space2[i][j-1] - space2[i-1][j-1] + (space[i][j]-'0');
		}
	}
	for(int size = 1 ; size <= n ; size++){
		for(int i = size ; i <= n ; i++){
			for(int j = size ; j <= n ; j++){
				if(space2[i][j]+space2[i-size][j-size]-space2[i-size][j]-space2[i][j-size] == size*size){
					furniture[size]++;
					cnt++;
				}
			}
		}
	}
	printf("total: %d\n",cnt);
	for(int i = 1 ; i <= n ; i++){
		if(furniture[i] == 0)break;
		printf("size[%d]: %d\n",i, furniture[i]);
	}
	return 0;
}
