#include <stdio.h>
#include<string.h>
int main()
{
	int n;
	scanf("%d", &n);
	int out[n][n];
	int y = n;
	memset(out,0, (n*n)*sizeof(int));
/*	for (int i=0; i<n; i++)
	{
		for(int j=0; j<2*y-1+i; j++)
		{
			if(j==0||j==2*y-2+i)
			{
				out[j][i] = y;
				out[j][2*n-2-i] = y;
			}
		y--;
	}
*/
	out[1][2] = 3;
	for (int i=0; i<2*n-1; i++)
	{
		for (int j=0; j<2*n-1; j++)
			printf("%d ", out[i][j]);
		printf("\n");
	}
	return 0;
}
