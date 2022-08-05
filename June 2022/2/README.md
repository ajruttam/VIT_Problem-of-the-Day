# Lexicographically Ordered Sentences

A sentence is said to be lexicographically ordered if the words of the sentence is either
in lexicographically ascending or lexicographically descending order. For example,
“apple is red” is in lexicographically ascending order and “zebra is animal” is in
lexicographically descending order. Given ‘n’ sentences, write a C++ program to print
lexicographically ordered sentences.

#### Hint

When cin and getline are mixed, we have to clear the buffer using ignore function.

For example,

```cpp
cin>>n;
cin.ignore();
getline(cin,s);
```

This problem can be quickly solved with string in STL. STL is Standard Template
Library that has got generic functions, classes and algorithms.

- To use string, add `#include<string>`
- We can create object and array of objects for string
- To read a string s with spaces use `getline(cin, s)`;
- A string object can be intialized to empty as string `s=""`;
- length is a member function of string that gives the number of characters in it
- You can access ith character of a string object s as `s[i]` – Subscript operator is
overloaded
- A character ‘c’ can be added to a string ‘s’ by `s=s+c`;
- Two strings s1 and s2 can be compared using `<, >` and `==`

#### Sample Code

```cpp
int main()
{
    string sen1;
    string w1,w2;
    sen1="";
    sen1=sen1+'a';
    getline(cin,sen1);
    cin>>w1>>w2;
    int len=sen1.length();
    if(w1<w2)
        cout<<"W1 is lexicographically less than w2";
}
```

#### Input Format

First line contains the number of sentences, n

Next ‘n’ lines contain the sentences

#### Output Format

Print the sentences that is in some lexicographical order