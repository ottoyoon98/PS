#include <stdio.h>
int main() {
	int n;
	char input1[10],input2[10],empty[10];
	int s_t, e_t;
	int s_time=0, e_time=24*60;
	for(int i = 0 ; i < n ; i++){
		scanf("%s",input1);
		scanf("%s",empty);
		scanf("%s",input2);
		s_t=((input1[0]-'0')*10+(input1[1]-'0'))*60+(input1[3]-'0')*10+(input1[4]-'0');
		e_t=((input2[0]-'0')*10+(input2[1]-'0'))*60+(input2[3]-'0')*10+(input2[4]-'0');
		printf("%d %d\n\n",s_t,e_t);
		if(s_t > s_time)s_time = s_t;
		if(e_t < e_time)e_time = e_t;
	}
	printf("%d %d\n\n",s_t, e_t);
	int s_h = s_time/60, s_m = s_time%60, e_h = e_time/60, e_m = e_time%60;
	if(s_h < 0)printf("0");
	printf("%d:",s_h);
	if(s_m < 0)printf("0");
	printf("%d ~ ",s_m);
	if(e_h < 0)printf("0");
	printf("%d:",e_h);
	if(e_m < 0)printf("0");
	printf("%d\n",e_m);

	return 0;
}


11111111111111111111111111111111111111111111111111
12586269025
