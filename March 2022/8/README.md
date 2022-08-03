# Secret Agent and Code Word

A secret agent is a government employee whose job involves gathering secret
information about the governments of unfriendly foreign countries. A secret
agent ‘X’ emailed a sentence ‘S’ with a code word ‘W’ to his head office. Only
one word of the sentence 'S' is real and others are fake. The agent ‘X’ also
mailed a sentence as a clue - if I tell you any one character ‘C’ of the code word
'W', then you would find exactly two words with ‘C’ in it, those words will have
same number of vowels and one of them is ‘W’.

For example, if the senetence ‘S’ mailed by agent ‘X’ is "AIM DUE OAT TIE
MOD", then TIE is the code word. Due to the following reasons:

| Word 'W' | Letter in word 'C' | Words with 'C' in it | Number of Vowels in the words |Status (Consider/Reject) of pair of words| Status (Consider/Reject)of pair of words |
|---|---|---|---|---|---|
|AIM|A|AIM, OAT|AIM – 2, OAT – 2|Consider||
|AIM|I|AIM, TIE|AIM – 2, OAT – 2|Consider||
|AIM|M|AIM, MOD|AIM – 2, MOD – 1|Reject|Reject|
|DUE|D|MOD, DUE|DUE - 2, MOD – 1|Reject|Reject|
|OAT|O|OAT, MOD|OAT – 2, MOD – 1|Reject|Reject|
|MOD|M|MOD, AIM|MOD – 1, AIM – 2|Reject|Reject|
|TIE|T|OAT, TIE|OAT – 2, TIE – 2|Consider||
|TIE|I|TIE, AIM|TIE – 2, AIM – 2|Consider||
|TIE|E|TIE, DUE|TIE – 2, DUE – 2|Consider|Consider|

#### Input Format

First line contains the sentence with codeword

#### Output Format

First line should contain the code word

#### Boundary Conditions

Length of the sentence < 200

Length of each word in the sentence<10

Number of words in each sentence <20