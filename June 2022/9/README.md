# Element Names and Symbols

A child is studying sixth class and he has got a list of elements and the
corressponding elements in his science book. It will be helpful to make
him to learn if a program could give the name of the element if symbol
is given vice versa. Given the elements and their symbols in the child’s
book, write a C++ program to print the name or symbol as required. For
example, if there are five elements with name and symbol as (zinc, zn),
(sulphur, s), (chlorine, cl), (sodium, na) and (tin, sb) and symbol is
given as sb then print tin.

#### Hint

This problem can be quickly solved with map in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- To use map, add `#include<map>`
- We have to give the data type of key and value during object
creation. For example, `map<int, int> m` will create a map that can
store an integer key and an integer value.
- Value can be inserted into the map m as `m[key] = value`
- To check if a key is present in a map, use count function. It returns
0 – if key is not present and 1 – otherwise
- To take the value of an existing key in the map use `value = m[key]`

#### Input Format

First line contains the number of elements in his book, n

Next ‘n’ lines contain name of element followed by symbol separated by
a space

Next line choice of query, 1 – symbol of element will be given 2- name
of element will be given

#### Output Format

Print Symbol or Element name if present otherwise print “Not found”