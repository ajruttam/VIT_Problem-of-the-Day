# New Number System

A new k – base number system using the symbols 0, 1, 2, ..., k-1 is developed.
Each number in the k-base number system is separated by a comma. Let
a ,a ,a be a number in k-base number system where a f ε {0, 1, 2, ..., k-1} then
value of the number in decimal number system is a *k +a *k +a *k . In a 18-
based number system, value of the number 16, 17, 15 is 15*18 +17*18 +15*18 .
Given two numbers in k-base number system, write a code to print the sum of
the numbers in k-base system.

For example, if the two numbers n1 and n2 to base 9 are 6,8,7 and 7,8,0 then
the sum of n1 and n2 are 4,8,8.

#### Note:

Use atoi for string to integer convesion. Refer the below code for reference

```cpp
#include <iostream>
using namespace std;
int main ()
{
    char s[100];
    cin>>s;
    int i=atoi(s);
    cout<<i+10;
}
```

#### Input Format

First line contains the base of number system, k

Next line contains the number n1 in k-base number system

Next line contains the number n2 in k-base number system

#### Output Format

Print the sum of n1 and n2 in k-base number system