# Distribute T-Shirts in a Marathon

A marathon is being conducted by a NGO in Chennai. T-Shirts with the theme
of the marathon and a number is given to the participants. The participants are
given the T-Shirts in the order of their arrival and new T-Shirts are also
continuously brought-in to the venue. T-Shirts are arranged one above the
other vertically and they are distributed from top to bottom. Three operations
are possible partcipant-entry, t-shirt-arrival and distribute t-shirt.

**Participant-entry** - Some ‘p’ number of participants are arrived and they are
made to wait for t-shirt distribution.

**T-shirt arrival** – Some ‘m’ number of t-shirts are brought to the venue and
arranged on a table. Always t-shirts arrived recently will be on the top

**Distribute-t-shirt** – Some ‘k’ number of t-shirts are distributed to ‘k’
participants, print name of the participant and t-shirt number

Given a sequence of operations performed, write a C++ code to carry out and
print the details of t-shirts distributed to partcipants during distribute-t-shirt
operation.

#### Illustration

If the input is

7

1

2

Name1 Name2

2

3 6 9 4

1

3 Name3 Name5 Name4

2

7 8 5 1 45 56 78 12

1

2 Name12 Name6

1

1 Name8

3

4

then the desired output is

Name1 12

Name2 78

Name3 56

Name5 45

#### Input Format

First line contains the number of operations, n

Details for ‘n’ operations are given. Code for operations, 1- Participant-entry, 2 -
T-shirt arrival and 3 – Distribute-t-shirt

For option 1, next line will contain the number of participants entered currently,
n, followed by ‘n’ names

For option 2, next line will contain the number of t-shirts arrived, m, followed by
‘n’ numbers written on the t-shirts

For option 3, next line contains the value of k

#### Output Format

For option 3, print the name and the t-shirt number given for the participant
separated by a space