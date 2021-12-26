#include <stdio.h>
#include <stdlib.h>
int D[10000], from[10000];
int fibo(int y,int mode){
	int n;
	   int x[200]={0,}, temp, max;
		    x[1] = x[2] = 1;
		        x[3] = 3;
			    n = 3;
			        while(x[n]+x[n-1] <= y){
					        x[n+1] = x[n] + x[n-1];
						        n++;
							    }
				    if(y == 2) x[++n] = 2;
				        while(x[n] != y){
						        max = 0;
							        for(int i = 1 ; i < n ; i++){
									            temp = x[i] + x[n];
										                if(max < temp && temp <= y){
													                max = temp;
															            }
												        }
								        x[++n] = max;
									    }
					    if(mode == 1){
						            for(int i = 1 ; i <= n ; i++){
								                printf("%d ", x[i]);
										        }
							        }
					        return n;
}
int find(int n)
{
	    if(D[n] != 0){
		            return D[n];
			        }
	        D[n] = fibo(n, 0);
		    from[n] = -1;
		        if(n/2 > 3 && D[n] > find(n/2)+2){
				        D[n] = find(n/2)+2;
					        from[n] = n/2;
						    }
			    if(n/36 > 3 && D[n] > find(n/3)+3){
				            D[n] = find(n/3)+3;
					            from[n] = n/3;
						        }
			        return D[n];
}
int path(int n)
{
	    if(from[n] == -1){
		            fibo(n, 1);
			        }
	        else
			    {
				            path(from[n]);
					            if(from[n] == n/2){
							                printf("%d ", from[n]+(n%2));
									            printf("%d ", n);
										            }
						            if(from[n] == n/3){
								                if(n%3!=0){
											                printf("%d %d ", from[n]+1, from[n]*2+1);
													            }
										            else printf("%d %d ", from[n], from[n]*2);
											                printf("%d ", n);
													        }

							        }
		    return 0;
}
int main()
{
	    int y;
	        scanf("%d",&y);
		    find(y);
		        path(y);
			    return 0;
}

