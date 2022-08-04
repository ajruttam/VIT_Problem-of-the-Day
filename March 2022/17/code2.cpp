#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int v,n,m,w;
    cin >> v >> n >> m;
    char d[7][10] = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
    cout << d[(abs(n - v%7 + 7) + m%7)%7];
    return 0;
}
