# Detailed Periodic Table

The school wants the child to know few more details about five
elements in each period of periodic table. So they ask the child to learn
symbol, group, period, block, atomic number and state of the element at
20°C . Given the details of the five elements in each period (except
period 1 – only two elements), period number and symbol of the desired
element, write a C++ program to print the other details of the desired
element.

#### Hint

This problem can be quickly solved with map in STL. STL is Standard
Template Library that has got generic functions, classes and algorithms.

- Using map of maps (that is map within map) will lead to simple
code
- To use map, add `#include<map>`
- We have to give the data type of key and value during object
creation. For example, `map<int, int> m` will create a map that can
store an integer key and an integer value.
- Map can also have key and values of objects of classes such as
string, vector etc.
- It is straightforward to have user defined data type as value of a
map and we can also have a vector of userdefined datatypes as
values
- A map can also have another map as value
- Value can be inserted into the map m as `m[key] = value`
- Value can also be inserted into a map using insert function, for
example to insert a key k and value v into a map m, we can write
`m.insert({k, v})` where curly braces around k and v creates a pair to
insert into the map
- To check if a key is present in a map, use count function. It returns
0 – if key is not present and 1 – otherwise
- To take the value of an existing key in the map use `value = m[key]`

#### Input Format

Details of elements is given in the following order - Name, Symbol,
group, block, atomic number and state of the element at 20 °C

First two lines contain the details of the five elements in period 1

Next five lines contain the details of the five elements in period 2

Next five lines contain the details of the five elements in period 3

Next five lines contain the details of the five elements in period 4

Next five lines contain the details of the five elements in period 5

Next five lines contain the details of the five elements in period 6

Next five lines contain the details of the five elements in period 7

Next line contains the period of the desired element

Next line contains the symbol of the desired element

#### Output Format

Print name, group, block, atomic number and state of element
separated by a space