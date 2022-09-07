"""
Merge Sort
"""
#check this
def Merge(numbers, left, middle, right):
    n1=middle-left+1
    n2=right-middle
    Left=[0,]*n1
    Right=[0,]*n2
    for i in range(n1):
        Left[i]=numbers[left+i]
    for i in range(n2):
        Right[i]=numbers[middle+1+i]
    i=0
    j=0
    k=left
    while i<n1 and j<n2:
        if Left[i]<=Right[j]:
            numbers[k]=Left[i]
            i+=1
        else:
            numbers[k]=Right[j]
            j+1
        k+=1
    while i<n1:
        numbers[k]=Left[i]
        i+=1
        k+=1
    while j<n2:
        numbers[k]=Right[j]
        j+=1
        k+=1


def MergeSort(numbers, left, right):
    if left<right:
        middle=(left+right-1)//2
        MergeSort(numbers, left, middle)
        MergeSort(numbers, middle+1,right)
        Merge(numbers, left, middle, right) 
    return(numbers)
    

numbers=[1,9,2,8,3,7,4,6,5]
print(MergeSort(numbers,0,9))