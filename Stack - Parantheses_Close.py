"""
Stack

Question:
Given a string containing only parantheses, determine if it is valid. The string is valid if all parantheses close.

Constraints:
does an empty string count?

Test cases:
""  # True 
"{[()]}" # True
"{([)]}" # False
"{[()" # False
"{[()()]}" # True
"}}}" # False
"""

def checkBracket(s):
    parans={'{':'}','(':')','[':']'}
    if len(s)=="":
        return True
    brackets=[]
    for i in s:
        if i in parans:
            brackets.append(i)
        else:
            if len(brackets)==0:
                return False
            check=brackets.pop()
            if parans[check]!=i:
                return False
    return len(brackets)==0

print(checkBracket(")]}"))
