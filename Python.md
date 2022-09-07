## Dictionary
key:value pairs

# Ways to create dictionary
dict1=dict()
dict2={}

Accessing value from key, insertion and deletion, time complexity= O(1)

Hash tables are the underlying data structures of dictionaries.
A hash table is a way of doing key-value lookups. You store the values in an array and then use a hash function to find the index of the array cell that corresponds to your key-value pair.
To avoid collision:
Method 1: Append the key value to the linked list. In this case, the searching time complexity can be O(n) for a bad hashing function.
Method 2: Linear probing go to the next available location. If at the last index, go to the beginning index.

adding if hashing is a linked list: amotised O(1)

# Deleting a value from dictionary
dict1.pop('key') -> returns the poped value
dict1.popitem() -> randomly deletes one key value and returns them both
dict1.clear() -> delete all pairs from the dictionary. does not return anything
dict1.del('key')-> deletes only key and value

Time complexity: amortized O(n)

# Methods in dictionary
dict1.copy -> shallow copy of dictionary
dict1.fromkeys(sequence[],value <optional>) -> creates new dictionary with given sequence
Ex. dict1={}.fromkeys([1,2,3],0)
dict1.get(key, value if key not found) By default returns null.
dict1.items() -> returns key value tuple pairs
dict1.keys()-> list of keys
dict1.values() -> list of values
dict.update(another dictionary/tuples) -> extend another dictionary
dict1.setdefault(key, defaultvalue) -> if key then sets value if not inserts key and sets value
all(dict1)-> like AND if all true or empty=true
any(dict1)-> like OR
len()
sorted() k=len -> sorts based on length of keys



# interesting to try this out - enumerate()

## Linked Lists

# Types of Linked Lists
1. Singly Linked List
value(head) and reference to next node(tail). Reference of last node is NULL

2. Circular Singly Linked List
value(head) and reference to next node(tail). Reference of last node is to the first node.

3. Doubly Linked List
reference to previous node(tail), value(head) and reference to next node(tail). Reference of last node is NULL

4. Circular Doubly Linked List
reference to previous node(tail), value(head) and reference to next node(tail). Reference of last node is to the first node.

## Recursion

# Tail recursion
Depends on the engine to remove the original call stack. Is it supported in Python?
Normal recursion space: O(N)
With tail recursion: O(1)

Normal recursion example faction
def normalRecursion(x):
    if x<=1:
        return 1
    return(x* normalRecursion(x-1))

With Tail recursion
def tailRecursion(x, totalSoFar=1):
    if x==0:
        return totalSoFar
    return tailRecursion(x-1, totalSoFar*x)

## Sorting Algorithm
Elementary sorts
- Bubble sort
Time: O(n^2)
Space: O(1)
- Selection sort
Time: O(n^2)
Space: O(1)
- Insertion sort
For when the array is almost completely sorted
Time: O(n^2)
Space: O(1)

Divide and Conquer
- Quick sort
Time: O(nlogn)
Space: O(1)
- Merge sort
Time: O(nlogn)
Space: O(n)

- Radix sort
- Heap sort
- Counting sort

## Interesting facts about Python
Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort.

## Trie
Usually used for strings and characters
A tree that stores information in an hierarchy with no repetitive node.
Uses
- Spelling checker
- Auto completion

# Operations on Trie
1. Creating
2. Inserting
3. Searching a string
4. Deletion