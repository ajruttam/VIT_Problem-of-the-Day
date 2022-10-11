#include <iostream>
using namespace std;

int main(){
    int n, s = 0;
    cin >> n;
    for (int i = 2; i < n; i++){
        int f = 1;
        for (int j = 2; j <= i/2; j++){
            if (i%j == 0)
            {
                f = 0;
                break;
            }
        }
        if (f) s+= i;
        if (n > s) continue;
        else if (n == s) cout << "Yes";
        else cout << "No";
        break;
    }
    return 0;
}
