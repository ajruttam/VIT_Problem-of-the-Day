#include <stdio.h>
int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);
        char x[20];
        scanf("%s", x);
        for (int i = 0; i < n; i++){
            if (x[i] >= 65 && x[i] <= 90)
                x[i] += 32;
        }
        int c = 0;
        for (int i = 0; i < n-1; i++){
            if (x[i] == x[i + 1])
                c++;
        }
        printf("%d\n",c);
    }
}
