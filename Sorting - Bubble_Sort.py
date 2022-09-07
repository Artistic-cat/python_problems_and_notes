"""
Bubble sort
"""
def bubbleSort(numbers):
    length=len(numbers)
    for i in range(length):
        for j in range(length-i):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return(numbers)
    
numbers=[1,9,2,8,3,7,4,6,5]
print(bubbleSort(numbers))