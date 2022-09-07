"""
ARRAYS
Two Sum
Level:Easy

Question:
Given an array of integers, return the indices of the two number that add up to a given target.

Example:
arr=[3,5,7,1,6]
target= 13

ans: [2,4]
"""

def FindTheTarget(arr,target):
    addition=dict()
    for i in range(len(arr)):
        if target-arr[i] in addition:
            return ([addition[target-arr[i]],i])
        else:
            addition[target-arr[i]]=i

arr=list(map(int,input().split()))
target=int(input())
        
print(FindTheTarget(arr,target))

# Complexity: O(n)
