// works for single digit numbers only
// cpp code using stack

#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t--){
        string s;
        cin >> s;
        stack <string> ans;
        int i = 0;
        while (1){
            if (s[i] == ']'){
                i++;
                string a = "";
                while (ans.top() != "["){
                    a = ans.top() + a;
                    ans.pop();
                }
                ans.pop();
                int n = stoi(ans.top());
                ans.pop();
                string aa = "";
                for (int j = 0; j < n;j++)
                    aa += a;
                ans.push(aa);
            }
            else{
                ans.push(string(1,s[i]));
                i++;
            }
            if (i == s.size()){
                string a;
                while (!ans.empty()){
                    a = ans.top() + a;
                    ans.pop();
                }
                ans.push(a);
                break;
            } 
        }
        cout << ans.top() << endl;
    }
}
