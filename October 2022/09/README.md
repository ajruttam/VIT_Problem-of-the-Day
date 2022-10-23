# Dictionary Rank

Write a computer program which prints the dictionary rank of a given word
which is made up of all unique letters. 

For example:

Let us consider the word “MOTHER”. We start with the first lowest letter which
is E. Thus, the letters made with E as the first letter would be 5! = 120.
Similarly, the next lowest letter after E is H. Fix H at first place, again the
number of combinations would be 5! = 120. After this, the next letter after H is
M. Now, in this case, this aligns with the required word (MOTHER).
Now, instead of calculating all the combinations. We first fix the second letter. Alphabetically, this would be E. Now, the total number of combinations with
these two letters fixed are 4! = 24 then second letter alphabetically is H with
same combination that is 4! = 24. The next available letter would be O. Again,
MO aligns with the word ‘MOTHER’. So, now, we will try to fix 3 letters and
then find the combinations. Again, alphabetically, we have E (thus, fixing
MOE), we have total combinations as 3! = 6, same goes for H and R with
combinations as 6 each. Now, the next letter would be T. This aligns with the
word ‘MOTHER’. Now, we fix 4 letters. Thus, the first available letter would be
E (MOTE is fixed). Thus, we have 2 combinations possible (2! = 2). Now, the
next letter would be H, again MOTH aligns with the word MOTHER. Now, the
next available letter would be E aligns with the word MOTHER. Thus, we have
all the combinations.

Sum up all combinations gives 120 + 120 + 24 + 24 + 6 + 6 + 6 + 2 = 308.
Since, there are 308 combinations before the word, ‘MOTHER’. The rank of the
word MOTHER is 308 + 1 =309.

#### Input format

First line takes the word as input.

#### Output format

Print the dictionary rank of the given word
