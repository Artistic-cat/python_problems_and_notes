"""
Almost a palindrome

Question:
Given a string, determine if it is almost a palindrome. A string is almost a palindrome if it becomes a palindrome by removing one letter. Consider only alphanumeric characters and ignore case sensitivity.

Constraints:
Is a palindrome is also almost a palindrome?

Test cases:
"" # True
"a" # True
"ab" # True
"raceacar" # True
"abccdba" # True
"abcdefdba" # False
"""

def validPalindrome(s,left,right):
    while(left<right):
        if (s[left!=s[right]]):
            return False
        left+=1
        right-=1
    return True
def main():
    s="ab"
    left=0
    right=len(s)-1

    while(left<right):
        if(s[left]!=s[right]):
            return(validPalindrome(s,left+1,right) or validPalindrome(s,left,right-1))
        left+=1
        right-=1
    return(True)
print(main())