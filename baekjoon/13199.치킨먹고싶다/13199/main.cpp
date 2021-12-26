#include <stdio.h>

using namespace std;

int chicken(int p, int m, int f, int c)
{
    int moreChicken = 0;
    int a0 = m/p;
    double Ca = 0, Cb = 0;
    Cb = a0+(a0*c/f);
    Ca = a0/(1-(double)c/f);
    moreChicken = Ca-Cb;
    return moreChicken;
}
int main()
{
//    freopen("input.txt","r",stdin);
//    freopen("output.txt","w",stdout);
    int T, p, m, f, c;
    scanf("%d",&T);
    for(int i = 0 ; i < T ; i++){
        scanf("%d %d %d %d", &p, &m, &f, &c);
        printf("%d\n",chicken(p, m, f, c));
    }

    return 0;
}
