#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int hx, hy, mx, my, nh, nm;
	cin >> hx >> hy >> mx >> my;
	nh = (hx - 1) * 4 + hy/5;
	nm = (mx - 1) * 20 + my;
	if (nh == 0)
		nh = 12;
	cout << setfill('0') << setw(2) << nh << endl << setfill('0') << setw(2) << nm;
	return 0;
}
