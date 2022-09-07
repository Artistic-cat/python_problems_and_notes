"""
Selection Sort
Pick the sortest item and push it to the top
"""

def SelectionSort(array):
    length=len(numbers)
    for i in range(length):
        min=i
        for j in range(i+1,length):
            if array[j]<array[min]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array

numbers=[1,9,2,8,3,7,4,6,5]
print(SelectionSort(numbers))