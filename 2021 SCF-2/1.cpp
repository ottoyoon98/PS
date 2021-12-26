#include <stdio.h>
int main() {
	int n;
	char Time[10];
	int pTime, song[100100]={0,};
	int maxCnt, maxI;

	scanf("%d %s",&n,&Time);
	pTime = ((Time[0]-'0')*10+(Time[1]-'0'))*60*60+((Time[3]-'0')*10+(Time[4]-'0'))*60+((Time[6]-'0')*10+(Time[7]-'0'));
	for(int i = 0 ; i < n ; i++){
		scanf("%s",Time);
		song[i] = ((Time[0]-'0')*10+(Time[1]-'0'))*60+((Time[3]-'0')*10+(Time[4]-'0'));
	}

	int s, e, sum=0;
	s = 0;
	e = 0;
	maxCnt = 0;
	maxI = 0;
	while(s < n){
		while(e < n-1 && sum+song[e] < pTime){
			sum = sum+song[e];
			e++;
		}
		if(e-s+1 > maxCnt){
			maxCnt = e-s+1;
			maxI = s;
		}
		sum-=song[s];
		s++;
	}
	printf("%d %d\n",maxCnt, maxI+1);
	return 0;
}
