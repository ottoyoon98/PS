#include <stdio.h>
int function(int a,int b);
void main(){
	int c;
	c = function(1, 2);
}
int function(int a, int b){
	char buffer[10];
	a=a+b;
	return a;
}
