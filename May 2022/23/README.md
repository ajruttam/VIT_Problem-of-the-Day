# Generate Letters

In a game a string S is given to child and the child is asked to check if it can put
each letter of the string in sequence in the boxes arranged in two rows so that
the letters in the boxes placed in the same column are same.

|1|2|3|4|5|
|---|---|---|---|---|
|10|9|8|7|6|

That is if there are 10 charcters in the string then the child can place them in the
order shown above. If the characters in the string are not in such a way that this
can be done then new characters are to be added to the string at the end to
achieve this.

For example, if the string is ab then string is expanded to abba to achieve this.
The number of boxes needs to be minimum and no character can be removed
from the string.

#### Input Format

First line contains the string, s

#### Output Format

First line cotains the string that can achieve the arrangement