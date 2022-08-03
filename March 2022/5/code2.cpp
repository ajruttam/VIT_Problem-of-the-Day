#include <iostream>
using namespace std;
int main()
{
	int x;
	cin >> x;
	if (x % 12)
		cout<<(x / 12 + 1) * 12 - (x % 12) + 1<<endl;
	else
		cout<<(x / 12) * 12 - 12 + 1<<endl;
	if (x % 6 == 0 || x % 6 == 1) cout<<"Green";
	else if (x % 6 == 2 || x % 6 == 5) cout<<"Orange";
	else cout<<"Blue";
	return 0;
}
