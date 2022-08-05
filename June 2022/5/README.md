# Reverse Greater

Here a word S1 is said to be greater than S2, if the number of characters in S1 is
greater than S2 or when the number of characters in S1 and S2 are equal and S1
is lexicographically greater than S2.

Given two sentences S1 and S2 with ‘n’ words in them, sentence S1 is said to be
reverse greater than sentence S2 if the first word in S1 is greater than the last
word (n word) in S2, second word is lexicographically greater than the last but
one (n word) in S2 .... last word in S1 is greater than the firt word in S2. For
example, if the sentences S1 and S2 are ‘thiss iss as sens’ and ‘sen a is this’ then
output should be Yes and if the sentences are ‘this is a sen’ and ‘sen a is this’
then the output should be No.

#### Hint:

This problem can be quickly solved with string in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- To use string, add `#include<string>`
- We can create object and array of objects for string
- length is a member function of string that gives the number of characters
in it
- `find_first_of(string,pos);` – will return the position of the first occurrence
of string s where pos is the position of the first character in the string to be
considered in the search and return -1 if cannot be found
- `find_last_of(string,pos);` – will return the position of the last occurrence of
string s where pos is the position of the last character in the string to be
considered in the search and return -1 if cannot be found
- `substr(i,n)` – will return a substring from position ‘i’ and of length ‘n’

#### Sample Code using String in STL

```cpp
#include<iostream>
using namespace std;
#include<string>
int main()
{
    string s1,s2;
    int l,pos;
    getline(cin,s1);
    //get length of s1
    l=s1.length();
    //substring of length 3 from position 2
    s2 = s1.substr(2,3);
    //searched for first occurrence of string s2 in s1 from position 3
    l = s1.find_first_of(s2,3);
}
```

#### Input Format

First line contains first sentence S1

Next line contains second sentence S2

#### Output Format

Print Yes or No