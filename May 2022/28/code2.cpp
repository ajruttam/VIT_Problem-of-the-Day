#include <iostream>
using namespace std;

int main(){
    long int x;
    cin >> x;
    int sum = 0;
    while (x > 0){
        sum += x%10;
        x /= 10;
    }
    cout << 9 - sum%9;
}
