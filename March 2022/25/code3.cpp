#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    cout << ((n % 4 == 0) || (n % 4 == 3) ? 0 : 1);
    return 0;
}
