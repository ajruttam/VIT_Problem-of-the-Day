#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int x1,y1,x2,y2,x3,y3,x4,y4,ab,bc,cd,da,ac,bd;
    cin>>x1>>y1>>x2>>y2>>x3>>y3>>x4>>y4;
    ab = sqrt((pow((x1 - x2),2) + pow((y1 - y2),2)));
    bc = sqrt((pow((x3 - x2),2) + pow((y3 - y2),2)));
    cd = sqrt((pow((x3 - x4),2) + pow((y3 - y4),2)));
    da = sqrt((pow((x1 - x4),2) + pow((y1 - y4),2)));
    ac = sqrt((pow((x1 - x3),2) + pow((y1 - y3),2)));
    bd = sqrt((pow((x4 - x2),2) + pow((y4 - y2),2)));
    cout << ((ab == cd && bc == da && ac == bd)? "Yes" : "No");
    return 0;
}
