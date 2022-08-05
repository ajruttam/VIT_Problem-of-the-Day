# Check Shuffled Sentence

Given two sentences S1 and S2 formed with a set of distinct words,
check if S1 is a shuffled sentence of S2. For example, if S1 = “this is a
book” and S2 = “book is this a” then S1 is a shuffled sentence of S2.

#### Hint

This problem can be quickly solved with string in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- To use string, add `#include<string>`
- We can create object and array of objects for string
- To read a string s with spaces use `getline(cin, s)`;
- A string object can be intialized to empty as string s="";
  length is a member function of string that gives the number of
  characters in it
- You can access ith character of a string object s as `s[i]` – Subscript
  operator is overloaded
- A character ‘c’ can be added to a string ‘s’ by `s=s+c`;

#### Sample Code

```cpp
int main()
{
    string sen1;
    sen1="";
    sen1=sen1+'a';
    getline(cin,sen1);
    int len=sen1.length();
}
```

#### Input Format

First line contains the sentence, S1

Next line contains the sentence, S2

#### Output Format

Print Yes if S1 is shuffled a sentence of S2 and No otherwise
