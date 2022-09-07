"""
ARRAYS
Container with most water
Level: Medium

Question:
You are given an array of positive integers where each integer represents the height of a vertical line on a chart.
Find two lines which together with the x-axis forms a container that would hold the greatest amount of water.
Return the area of water it would hold.

Consider:
- lines don't count as area

"""

arr=[1,8,6,2,9,4]
# area= 32
start=0
end=len(arr)-1
maxArea=0
for i in range(len(arr)):
    
    if arr[start]>arr[end]:
        maxArea= (end-start)*arr[end]
        pass
    else:
        maxArea= (end-start)*arr[start]
        pass
print(maxArea)