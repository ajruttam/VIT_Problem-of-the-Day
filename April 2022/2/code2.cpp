#include <iostream>
using namespace std;

int main(){
	int p, s, n;
	cin >> p >> s >> n;
	int plants = p, water = p;
	for (int i = 1; i < n - 1; i += 2){
		plants += s;
		water += plants;
	}
	cout << plants << endl << water;
	return 0;
}
