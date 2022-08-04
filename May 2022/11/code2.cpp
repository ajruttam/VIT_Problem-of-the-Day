#include <iostream>
using namespace std;

int main(){
	int s, arr[6];
	cin >> arr[0] >> s;
	arr[3] = (s - 2 * arr[0])/2;
	arr[2] = (arr[0] - arr[3])/2;
	arr[1] = arr[0] - arr[2];
	arr[4] = arr[2] - arr[3];
	arr[5] = arr[3] - arr[4];
	
	for (auto i : arr)
		cout << i << " ";
		
	return 0;
}
