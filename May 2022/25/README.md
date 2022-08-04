# Nullify Bits

For a given integer, odd_bit_value is defined as the number of bits
which are '1' in odd position and even_bit_value is defined as the
number of bits which are '1' in even position. Nullification is a process
in which the 1's in odd position are made as zero if odd_bit_value is
lesser than even_bit_value and it makes 1's in even position as zeros
otherwise.

In this process, number of bits to be considered for this process is equal
to the minimum number of bits required to represent the number. The
right most bit of the number is considered to at poistion 1. For example,
if n is 12 - 1100, it becomes 4 and 15 becomes 5.

Given an integer, write a C++ program to print the number after
nullification.

#### Input Format

First line contains number, n

#### Output Format

Print the number after nullification