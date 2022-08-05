# Periods in Periodic Table

In a periodic table, all of the elements in a period have the same
number of atomic orbitals. For example, every element in the top row
(the first period) has one orbital for its electrons. Now the child we dealt
in yesterday’s problem has grown up and he is in eigth class. His school
wants him to remeber atleast five elements (except for the first period
where there are only two elements) in each period of the periodic table.
Given the period number, two elements in the first period and five
elements in other six periods, write a C++ program to read a period
number and print the elements under that particular period number.

#### Hint

This problem can be quickly solved with map in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- To use map, add `#include<map>`
- We have to give the data type of key and value during object
creation. For example, `map<int, int> m` will create a map that can
store an integer key and an integer value.
- Map can also have key and values of objects of classes such as
string, vector etc.
- Value can be inserted into the map m as `m[key] = value`
- To check if a key is present in a map, use count function. It returns
0 – if key is not present and 1 – otherwise
- To take the value of an existing key in the map use `value = m[key]`

#### Input Format

First line contains the name of the two elements under period 1 in
periodic table

Next line contains the name of the five elements under period 2 in
periodic table

Next line contains the name of the five elements under period 3 in
periodic table

Next line contains the name of the five elements under period 4 in
periodic table

Next line contains the name of the five elements under period 5 in
periodic table

Next line contains the name of the five elements under period 6 in
periodic table

Next line contains the name of the five elements under period 7 in
periodic table

Next line contains the period number, n

#### Output Format

Print name of the elements under period number n separated by a space