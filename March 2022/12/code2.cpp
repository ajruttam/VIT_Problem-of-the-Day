#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int l,u;
    cin>>l>>u;
    for (int a = l; a<=u; a++)
        for (int b = l; b<= u; b++)
            for (int c = l; c <= u; c++)
                if (a <= b && b <= c){
                    if (c*c - a*a - b*b == 0)
                        cout << a <<" "<< b << " " << c << " Exactly Pythagorean"<<endl;
                    else if (abs(c*c - a*a - b*b) == 1)
                        cout << a <<" "<< b << " " << c << " Very Close to Pythagorean"<<endl;
                    else if (abs(c*c - a*a - b*b) == 2)
                        cout << a <<" "<< b << " " << c << " Close to Pythagorean"<<endl;
                }
    return 0;
}
