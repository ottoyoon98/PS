#include <stdio.h>
int main()
{
	char buf[100];
	printf("input string: ");
	gets(buf);
	printf("check your input: %s\n",buf);
	return 0;
}
