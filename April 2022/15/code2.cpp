#include <iostream>
using namespace std;
int main()
{
    int t; cin >> t;
    while (t--)
    {
        int x,y,z;
        cin >> x >> y >> z;
        cout << y * (1 + (int) ((z - x) * 1.5/x)) << endl;
    }
    return 0;
}
