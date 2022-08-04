#include <stdio.h>
#include <math.h>
int main()
{
    int d;
    double x, y, b;
    scanf("%d %lf %lf", &d, &x,&y);
    for (int a = 0; a < d; a++)
    {
        b = pow(d*d - a*a, 0.5);
        if ((int) b == b)
        {
            if (a-1>x && x>1 && b-1>y && y>1)
            {
                printf("Safe");
                return 0;
            }
        }
    }
    printf("Unsafe");
    return 0;
}
