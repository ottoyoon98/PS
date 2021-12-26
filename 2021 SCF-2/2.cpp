#include <stdio.h>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
struct Edge
{
    int s, e, d;
};
int fo(const struct Edge &a, const struct Edge &b)
{
    if(a.d <b.d)return 1;
    return 0;
}
int findGroup(int h, int* group)
{
    if(group[h] == h)return h;
    else return group[h] = findGroup(group[h], group);
}
int main()
{
	int n, m;
	scanf("%d",&n);
    char a[20], b[20];
	int d;
	int group[20010]={0,};
	map <string, int> place;
	m = 0;
	struct Edge edge[20010]={0,};
	for(int i = 0 ; i < n ; i++){
		scanf("%s %s %d",a, b, &d);
		if(place.find(a) == place.end())place[a] = ++m;
		if(place.find(b) == place.end())place[b] = ++m;
		edge[i].s=place[a];
		edge[i].e=place[b];
		edge[i].d=d;
	}
	printf("%d",m);
	for(int i = 1 ; i <= m ; i++)group[i]=i;
	sort(edge,edge+n,fo);
	int ga,gb;
	int sum=0, cnt=0;
	for(int i = 0 ; i < n ; i++){
        ga = findGroup(edge[i].s, group);
        gb = findGroup(edge[i].e, group);
        if(ga == gb)continue;
        group[gb] = ga;
        sum+=edge[i].d;
        cnt++;
        if(cnt == m-1)break;
	}
	printf("%d",sum);
	return 0;
}
