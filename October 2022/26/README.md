# Distinct Array

Let F(S) denote the number of distinct elements in the array S. For
example, F(\[1, 2, 3, 2\]) = 3, F(\[1, 2\]) = 2.

You are given an array A containing N integers. Find if it is possible to
divide the elements of the array A into two arrays B and C such that :

+ Every element of the array A belongs either to array B or to array C.
+ F(B) = F(C).

#### Input Format

The first line of input will contain a single integer T, denoting the
number of test cases.

Each test case consists of two lines of input.

The first line of each test case contains an integer N — the
length of the array A.

The next line contains N space-separated integer A<sub>1</sub> , A<sub>2</sub> ,…,A<sub>N</sub>,
denoting the elements of the array A.

#### Output Format

For each test case, print YES if it is possible to divide the elements of
the array A into two arrays B, C satisfying all the conditions
and NO otherwise.

#### Constraints

1 ≤ T ≤ 10<sup>4</sup>

2 ≤ N ≤ 10<sup>5</sup>

1 ≤ A<sub>i</sub> ≤ N

The sum of N over all test cases won't exceed 2⋅10<sup>5</sup>
