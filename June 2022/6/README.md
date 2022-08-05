# Missed Data and Average

A mobile company collected data about usage of their mobile phones in various
cities of the country. The details were then arranged such that the distance
between the head office and the city is increasing. While data was entered they
missed a data of a city. Given the data entered, missed data position and missed
data, write a C++ program to print the data after insertion and average usage of
every three adjacent cities.

For example, if six data are entered 13, 16, 19, 31, 45 and 67, missed data
position is 2 and missed data is 50 then the data after insertion is 13, 50, 16, 19,
31, 45, 67 and average of three adjacent cities are 26.33, 28.33, 22.00, 31.67 and
47.67.

#### Hint

This problem can be quickly solved with vector in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- To use vector, add `#include<vector>`
- We can create object and array of objects for vector
- `size()` - Number of elements in a vector can be found
- `[]` - can be used to random access elements of a vector
- `begin()` - will give reference to the first element in the vector which can be
stored in an iterator
- `end()` - will give reference to one position next to last element in the vector
which can be stored in an iterator
- iterator for a integer vector with integer elements can be declared as
`vector<int>::iterator` it
- `+, -, ++, --, <, >, ==, !=` operators that can be used with iterators
- `insert(pos, e)` – Inserts the element ‘e’ at the given iterator position pos

#### Sample code

```cpp
#include<iostream>
using namespace std;
#include<vector>
int main()
{
    vector<int> v;
    v.push_back(11);
    v.push_back(12);
    vector<int>::iterator =v.begin();
    //to insert data at 5th position
    v1.insert(it+4,mis_data);
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<endl;
    }
}
```

#### Input Format

First few lines contain the data entered and it is ended by -1

Next to the line -1 is the missed postion

Next line contains the missed data

#### Output Format

First line contains data after inserting missing data separated by a tab

Next line contains average of three cities with precision of two decimal place
and separated by a tab

To print only two decimal places of variable f use:

```cpp
#include<iomanip>
cout<<fixed<<setprecision(2)<<f;
```