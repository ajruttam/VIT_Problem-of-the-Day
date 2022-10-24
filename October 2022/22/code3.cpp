#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        string x;
        cin >> x;
        for (int i = 0; i < n; i++){
            if (x[i] >= 65 && x[i] <= 90)
                x[i] += 32;
        }
        int c = 0;
        for (int i = 0; i < n-1; i++){
            if (x[i] == x[i + 1])
                c++;
        }
        cout << c << endl;
    }
}
