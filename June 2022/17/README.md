# Swap Coins

Given the ‘m’ coins held by ‘n’ children, write a C++ program to perform ‘k’
swap coins operations. During swap coins operation between two children, all
the coins held by one child is swapped with all coins of the other child. After
swap operations, print the coins held the children in the order as given in input.
For example, when there are five children with five coins as follows:

Name1 5 10 12 45 67

Name2 7 9 11 13 49

Name3 90 21 34 56 67

Name4 22 35 68 91 29

Name5 37 78 93 44 55

After three swaps between the children mentioned below:

Name3 Name5

Name2 Name1

Name5 Name4

Coins with the children left over are:

Name1 7 9 11 13 49

Name2 5 10 12 45 67

Name3 37 78 93 44 55

Name4 90 21 34 56 67

Name5 22 35 68 91 29

#### Hint:

This problem can be quickly solved using map and vector in STL. Vector has a
function swap which will swap elements of two vectors v1 and v2.

For example, `v1.swap(v2)` – will swap all elements of v1 and v2

#### Input Format

First line contains the number of children, n

Next ‘n’ lines contain the name of the child and the coins the coins held by the
child

Next line contains the value of k

Next ‘k’ lines contain the name of the two children whose coins are to be
swapped

#### Output Format

Print ‘n’ lines

In ith line, print name of the ith child and the coins in the hand of the ith child

**Note**: A space is there at the end of each line