# String Decoding

Given an encoded string,you have to return it’s decoded string. The encoding
rule is: k[encodedString], where the encoded_string inside the square
brackets is being repeated exactly k times. Note that k is guaranteed to be a
positive integer greater than 1. You may assume that the input string is always
valid; No extra white spaces, square brackets are well-formed, etc. Furthermore,
you may assume that the original data does not contain any digits and that
digits are only for those repeat numbers, k. For example, there won’t be input
like 3a or 2[4].

#### Input Format

First line of each input take a value of T, denoting number of testcases.

First line of each testcase contains the encoded string.

#### Output Format

Each decoded string should be printed in new line.

**Sample Test case 1**
```
3
3[a]2[bc]
3[a2[c]]
2[abc]3[cd]ef
```

**Output 1**
```
aaabcbc
accaccacc
abcabccdcdcdef
```
