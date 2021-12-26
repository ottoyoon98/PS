#include <stdio.h>
#include <string.h>

char list[1010][10010]={0,};
int alphabet[1010][30]={0,}, q_alpha[30]={0,};
int alpha_sum[1010][10010]={0,}, q_sum[30]={0,};

int main() {
	int n, q, len,qlen;
	scanf("%d", &n);
	for(int i = 0 ; i < n ; i++){
		scanf("%s",list[i]);
		len = strlen(list[i]);
		for(int j = 0 ; j < len ; j++) alphabet[i][list[i][j]-'a']++;
		alpha_sum[i][0]= 0;
		for(int j = 0 ; j < len ; j++) alpha_sum[i][j+1] = alpha_sum[i][j]+(list[i][j]-'a');
	}

	char query[101]={0,};
	int check, cnt;
	scanf("%d", &q);
	for(int queryI = 0 ; queryI < q ; queryI++){
		scanf("%s", query);
		//searching
		qlen = strlen(query);
		for(int i = 0 ; i < 26 ; i++) q_alpha[i] = 0;
		for(int i = 0 ; i < qlen ; i++) q_alpha[query[i]-'a']++;
		q_sum[0] = 0;
		for(int i = 0 ; i < qlen ; i++) q_sum[i+1] = q_sum[i]+(query[i]-'a');

		cnt = 0;
		for(int i = 0 ; i < n ; i++){
			check = 0;
			for(int j = 0 ; j < 26 ; j++){
				if(alphabet[i][j] < q_alpha[j]){
					check = 1;
					break;
				}
			}
			if(check == 1)continue;
			len = strlen(list[i]);
			for(int j = 0 ; j <= len-qlen ; j++){
				if(alpha_sum[i][j+qlen]-alpha_sum[i][j] != q_sum[qlen]-q_sum[0])continue;
				if((alpha_sum[i][j+qlen/2]-alpha_sum[i][j]) != (q_sum[qlen/2]-q_sum[0]))continue;
				if((alpha_sum[i][j+qlen]-alpha_sum[i][j+qlen/2]) != (q_sum[qlen]-q_sum[qlen/2]))continue;
				check = 0;
				for(int k = 0 ; k < qlen ; k++){
					if(list[i][j+k] != query[k]){
						check = 1;
						break;
					}
				}
				if(check == 1)continue;
				cnt++;
				break;
			}
		}
		printf("%d\n",cnt);
	}
	return 0;
}

