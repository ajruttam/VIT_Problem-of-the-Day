#include <iostream>
#include <string>
using namespace std;

int main(){
    string x;
    cin >> x;
    int f = 1;
    for (int i = 0; i < x.size(); i++){
        if (i == 2 or i == 3 or i == 4){
            if (!(x[i] >= 'A' and x[i] <= 'Z'))
                f = 0;
        }
        else{
            if (!(x[i] >= '0' and x[i] <= '9'))
                f = 0;
        }
    }
    if (f) cout << "YES" << endl << 2004 + stoi(x.substr(0,2));
    else cout << "NO";
}
