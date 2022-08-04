#include <iostream>
using namespace std;
int main()
{
    int n,idx;
    cin >> n;
    string s = "";
    char w;
    for (int i = 0; i < n; i++){
        cin >> w;
        s += w;
    }
    for (int i = 0; i < n; i++) s += s[i];
    cin >> w;
    for (int i = 0; i < n; i++){
        if (s[i] == w){
            idx = i;
            break;
        }
    }
    for(int i = idx + 1; i < idx + n; i++)
    {
        cin >> w;
        if (s[i] != w)
        {
            cout << "Shuffled";
            return 0;
        }
    }
    cout << "Not Shuffled";
    return 0;
}
