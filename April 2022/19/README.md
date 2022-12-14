# Stern-Brocot Sequence

Stern-Brocot Sequence is a sequence similar to fibanocci series. A sequence āaā is
built using the following rules:

- a<sub>0</sub> = 0
- a<sub>1</sub> = 1
- a<sub>2i</sub> = a<sub>i</sub>
- a<sub>2i+1</sub> = a<sub>i</sub> + a<sub>i+1</sub>

For example, the sequence of numbers 1, 1, 2, 1, 3 is a Stern-Brocot
Sequence and 1, 1, 2, 1, 3, 2, 3, 3, 4 is not a Stern-Brocot Sequence since the
eigth element is not as per rule. Given ānā numbers write a C++ code to find
out if it can be a Stern-Brocot Sequence when taken in order.

#### Input Format

First line contains the number of elements, n

Next line contains the elements separated by a space

#### Output Format

Print Yes if the elements form Stern-Brocot Sequence and print No and
the index of the first element which violates the rule