#include <iostream>
using namespace std;
int main()
{
    int n,l,c = 1;
    cin>>n;
    char ws[n][5];
    for (int i = 0; i < n; i++)
        cin>>ws[i];
    string s,w;
    cin>>s;
    for (int j = 0; j < 4; j++){
        cin>>l;
        w += s[l - 1];
    }
    for (int k = 0; k < n; k++){
        if (w == ws[k]) {
            cout<<"Valid";
            c = 0;
            break;
        }
    }
    if (c) cout<<"Invalid";
    return 0;
}
