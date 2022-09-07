#Maximum points on a line
#m=y2-y1/x2-x1
"""
Input
5
0 0
1 1
2 2
0 1
2 4

Output
3
"""

n=5
arr=[[0,0],[1,1],[2,2],[0,1],[2,4]]

dict1={}
maximum=0
for i in range(len(arr)-maximum-1):
    i_max=0
    for j in range(i+1,len(arr)):
        if arr[j][0]-arr[i][0]==0:
            slope= 999999#denominator=0, so some high number to denote infinity
        else:
            slope=float(arr[j][1]-arr[i][1])/float(arr[j][0]-arr[i][0])
        if dict1.has_key(slope):
            dict1[slope]+=1
        else:
            dict1[slope]=1
        i_max= i_max if i_max>dict1[slope] else dict1[slope]
    dict1.clear()
    maximum= maximum if maximum>i_max else i_max
print(maximum+1)
