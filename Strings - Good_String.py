"""
Question:
You are given a string S of length N, Q ranges of the form [L,R] in a 2D array range and a permutation arr containing numbers from 1 to N.
In one operation you remove the first character as per permutation. However, the positions of other characters will not change. Determine the minimum number of operations for the remaining string to be good

Notes
- A string is considered good if all the Q ranges have all distinct characters. Removed characters are not counted
- A range with all charactrs removed is considered to have all distinct characters
- The sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once
- 1-based indexing followed

Explanation
For the sample output:
N=8, Q=3, S="abbabaab"
arr=[6,3,5,1,4,2,7,8]
ranges=[[1,3],[4,7],[3,5]]

Sample input:
1
8 3
abbabaab
6 3 5 1 4 2 7 8
1 3
4 7
3 5

Sample output:
5

Time limit - 3.0s
Memory limit - 256MB

"""

def checkUnique(S):
    char_check={}
    for i in S:
        if i!="_":
            if i in char_check:
                return(False)
            else:
                char_check[i]=1
    return(True)

def goodString(S,arr,ranges):
    if ranges==[]:
        return(0)
    
    count=0
    while(checkUnique(S[ranges[0][0]-1:ranges[0][1]])==False):
        S=S[:arr[0]]+"_"+S[arr[0]+1:]
        count+=1
    return(count+goodString(S,arr[count:],ranges[1:]))

# T=int(input())
T=1
for _ in range(T):
  # N,Q=map(int,input().split())
  N,Q=8,3
  # S=input()
  S="abbabaab"
  # arr=list(map(int,input().split()))
  arr=[6,3,5,1,4,2,7,8]
  # ranges=[list(map(int,input().split())) for i in range(Q)]
  ranges=[[1,3],[4,7],[3,5]]

  out_=goodString(S,arr,ranges)
  print(out_)

