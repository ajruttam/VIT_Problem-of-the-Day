#include <iostream>
#include <vector>
using namespace std;

int main(){
	vector <int> v;
	int x;
	
	for (int i = 0; i < 10; i++)
	{
		cin >> x;
		v.push_back(x);
	}
	
	int e = ((v.at(5) - v.at(0)) + v.at(7))/2;
	int b = v.at(7) - e;
	int a = v.at(0) - b;
	int d = v.at(9) - e;
	int c = v.at(6) - d;
	
	cout << a << " " << b << " " << c << " " << d << " " << e ;
	return 0;
}
