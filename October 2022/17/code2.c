#include <stdio.h>

int main(){
	int n;
	scanf("%d", &n);
	if (n == 0 || n == 1)
		printf("impossible");
	else{
		for (int i = n; i > 0; i--){
			for (int j = 0; j < i; j++)
				printf("*");
			for (int j = 0; j < 2*(n-i+1)-1; j++)
				printf(" ");
			for (int j = 0; j < i; j++)
				printf("*");
			printf("\n");
		}
		for (int i = 2; i <= n; i++){
			for (int j = 0; j < i; j++)
				printf("*");
			for (int j = 0; j < 2*(n-i+1)-1; j++)
				printf(" ");
			for (int j = 0; j < i; j++)
				printf("*");
			printf("\n");
		}
	}
}
