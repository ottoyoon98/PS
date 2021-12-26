#include <stdio.h>
#include <algorithm>

using namespace std;

typedef struct _Content
{
	int watch_state;
	char genre;
	int x, y;
}CONTENT;

float genre_preference[10];

int sort_algorithm(const CONTENT &A, const CONTENT &B)
{
	if(A.watch_state < B.watch_state){
		return 0;
	}
	else if(A.watch_state == B.watch_state){
		if(genre_preference[A.genre-'A'] > genre_preference[B.genre-'A']){
			return 0;
		}
		else if(genre_preference[A.genre-'A'] == genre_preference[B.genre-'A']){
			if(A.x < B.x){
				return 0;
			}
			else if(A.x == B.x && A.y < B.y){
				return 0;
			}
		}
	}
	return 1;
}

int main()
{
	CONTENT contents[1100]={0,};
	char watch_input[150][50]={0,};
	char genre_input[150][50]={0,};
	int n,m;


	for(int i = 0 ; i < 5 ; i++){
		scanf("%f ",&genre_preference[i]);
	}
	scanf("%d %d",&n,&m);
	for(int i = 0 ; i < n ; i++){
		scanf("%s",watch_input[i]);
	}
	for(int i = 0 ; i < n ; i++){
		scanf("%s",genre_input[i]);
	}
	int cnt = 0;
	for(int i = 0 ; i < n ; i++){
		for(int j = 0 ; j < m ; j++){
			if(watch_input[i][j] == 'W')contents[cnt].watch_state = 1;
			else if(watch_input[i][j] == 'O')contents[cnt].watch_state = 2;
			else if(watch_input[i][j] == 'Y')contents[cnt].watch_state = 3;
			contents[cnt].genre = genre_input[i][j];
			contents[cnt].x = i;
			contents[cnt].y = j;
			cnt++;
		}
	}
	sort(contents, contents+cnt, sort_algorithm);
	for(int i = 0 ; i < n*m ; i++){
		if(contents[i].watch_state == 1)break;
		printf("%c %.1f %d %d\n", contents[i].genre, genre_preference[contents[i].genre-'A'], contents[i].x, contents[i].y);
	}
	return 0;
}
