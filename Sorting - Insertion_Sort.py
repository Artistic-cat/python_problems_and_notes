"""
Insertion Sort
For times when the array is almost completely sorted
"""

def InsertionSort(array):
    length=len(numbers)
    for i in range(1,length):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
    return(array)

numbers=[1,9,2,8,3,7,4,6,5]
print(InsertionSort(numbers))