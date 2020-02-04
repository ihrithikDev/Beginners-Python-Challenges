'''

Deja Vu 

 You aren't paying attention and you accidentally type a bunch of random letters
 on your keyboard. You want to know if you ever typed the same letter twice, or
 if they are all unique letters.

Task: 
If you are given a string of random letters, your task is to evaluate whether any 
letter is repeated in the string or if you only hit unique keys while you typing.

Input Format: 
A string of random letter characters (no numbers or other buttons were pressed).

Output Format: 
A string that says 'Deja Vu' if any letter is repeated in the input string, 
or a string that says 'Unique' if there are no repeats.

Sample Input: 
aaaaaaaghhhhjkll

Sample Output: 
Deja Vu


'''
letters = "abcdefghijklmnopqrstuvwxyz"


def Checker(string):

    string = string.replace(" ", "").lower()

    total = 0

    for l in letters:
        count = string.count(l)
        if count > 1:
            total += count

    if total > 0:
        print("Deja Vu")
    else:
        print("Unique")

string = input()
Checker(string)