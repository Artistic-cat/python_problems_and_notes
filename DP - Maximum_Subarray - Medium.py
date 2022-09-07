"""
DYNAMIC PROGRAMMING
MAximum Subarray
Level: Medium

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

def maxSubarray(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return(max(sum(arr), maxSubarray(arr[1:]), maxSubarray(arr[:-1])))
arr= [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarray(arr))

