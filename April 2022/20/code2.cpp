#include <iostream>

using namespace std;

int main(){
	int n, c1, c2;
	cin >> n >> c1 >> c2;
	
	cout << n * c1 + n * (n - 3)/2 * c2 ;
	return 0;
}
