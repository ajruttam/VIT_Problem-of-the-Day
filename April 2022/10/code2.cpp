#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	vector <int> v;
	int x {0};
	
	for (int i = 0; i < 3; i++)
	{
		cin >> x;
		v.push_back(x);
	}
	
	sort(v.begin(),v.end());
	
	cout << ((v.at(1) == 1)? v.at(0) - v.at(1) - v.at(2) : v.at(0) - v.at(1) * v.at(2));
	
	return 0;
}
