#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    char x;
    int n,m;
    float t;
    cin>>x>>n>>m>>t;
    cout << setprecision(2) << fixed;
    cout << ((x == 'l')?((abs(n - m) - 1)*t): ((abs(n - m) + 1)*t));
    return 0;
}
