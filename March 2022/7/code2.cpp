#include <iostream>
using namespace std;
int main()
{
	int n,m,c = 0;
	cin>>n>>m;
	for (int i = 1;i<=m;i++)
	if (m%i==0) c++;
	c%2? cout<<"On": cout<<"Off";
	return 0;
}

