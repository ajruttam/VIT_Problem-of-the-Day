#include <iostream>
using namespace std;

int main(){
    int n, s = 0;
    cin >> n;
    bool f = true;
    while (n>0){
        if (f)
            s += n%10;
        else
            s -= n%10;
        n /= 10;
        f = !f;
    }
    cout << abs(s);
}
