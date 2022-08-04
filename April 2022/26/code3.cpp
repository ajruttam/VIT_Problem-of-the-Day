#include <iostream>
using namespace std;
int main()
{
    int x,w1,w2,n,w;
    cin >> x >> w1 >> w2 >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> w;
        cout << (((w - x)%w1==0 || (w - x)%w2==0 || (w-x)%(w1+w2)==0)? 1 : 0) << " ";
    }
    return 0;
}
