#The Dutch National Flag Problem / Sort it up

"""
You are given a array arr, consisting of 0s,1s and 2s.
Sort the same array in place and return it, do not create a new array

Input
n - size of the array
arr- the array
20102

Output
Sorted array
00122

"""

arr=[2,0,1,0,2]
n=5

left_bound=0
right_bound=n-1
i=0
while i <= right_bound:
    if arr[i]==2:
        arr[i],arr[right_bound]=arr[right_bound],arr[i]
        right_bound-=1
    elif arr[i]==0:
        arr[i],arr[left_bound]=arr[left_bound],arr[i]
        left_bound+=1
        i+=1
    else:
        i+=1
print(arr)

#Complexity: 
