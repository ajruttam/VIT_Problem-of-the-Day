# Swap Details Entered

An web application was designed by a company to calculate the income
tax of its employees as per the latest budget. A form was designed to
enter the details of the employees and do income tax calculation. Since
the basic excemption limit, percentage of deductions etc differ based on
gender, separate forms are designed in the web application for male and
female. Number of fields to be entered and width of the fields to be
entered are same. By mistake both the genders have entered details in
the form for the other gender. Internally the details entered by each
employee is stored as a string with a delimiter in between. For males ‘:’
is used as the delimiter and for females ‘#’ is used as delimiter.

Given the strings of details of a male and a female employee, write a
C++ code to swap the corressponding fields and make it ready for
further processing.

For example, if the strings given are

50891:12378949:10000:ACZPJ9823B and

78191#45376107#10200#BFZPJ0453B then the output should be

78191:45376107:10200:BFZPJ0453B and

50891#12378949#10000#ACZPJ9823B


#### Hint:

This problem can be quickly solved with string in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- To use string, add `#include<string>`
- We can create object and array of objects for string
- length is a member function of string that gives the number of
characters in it
- `find(s, pos)` – will return the position of the string s from position
pos and return -1 if cannot be found
- `substr(i,n)` – will return a substring from position ‘i’ and of length
‘n’
- `replace (p1,p2,s)` – replaces part of the string from p1 to p2 by s

#### Sample Code using String in STL

```cpp
#include<iostream>
using namespace std;
#include<string>
int main()
{
    string s1,s2;
    int l,pos;
    cin>>s1;
    //get length of s1
    l=s1.length();
    //substring of length 3 from position 2
    s2 = s1.substr(2,3);
    //searched for string s2 in s1 from position 3
    l = s1.find(s2,3);
    //replace part of string three characters from position 4 by s2
    s1.replace(4,3,s2);
}
```

#### Input Format

First line contains the details entered by female with wrong delimiter

Next line contains the details entered by male with wrong delimiter

#### Output Format

First line contains the details entered by male with correct delimiter