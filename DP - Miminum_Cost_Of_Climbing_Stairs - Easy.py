"""
DYNAMIC PROGRAMMING
Miminum Cost Of Climbing Stairs
Level: Easy-Medium

Question:
For a given staircase, the i-th step is assigned a non-negative cost indicated by a cost array is assigned a non-negative cost indicated by a cost array.
Once you pay the cost for a step, youcan either climb one or two steps. Find the minimum cost to reach the top of the staircase. Your first step can either be the first or second step. 

How to know this is a dynamic programming problem:
- Minimum cost
- off all combinations (need to generate all paths)
- each step has branching similar branches

Dynamic programming steps:
- define a recursive formula
- optimse that top down (Memoizing)
- change that to an iterable formula with bottom up approach

Sample input:
arr=[20,15,30,5]

"""


# Formula formed: total_cost[i]= cost[i]+min(minCost[i-1],minCost[i-2])

# Step 1: Define a recursive function
 
"""
def minCost(cost,n):
    if n<0:
        return(0)
    if n==0 or n==1:
        return(cost[n])
    return(cost[n]+min(minCost(cost,n-1), minCost(cost,n-2)))

cost=[20,15,30,5]
cost.append(0)
n=4
print("Minimum cost to reach the top is:",minCost(cost,n))

"""
# Time complexity: O(2^n)
# Space complexity: O(N)

# Step 2: Memoizing
"""
def minCost(cost,n,saved_costs):
    if n<0:
        return(0)
    if n==0 or n==1:
        return(cost[n])
    if saved_costs[n]!=-1:
        return(saved_costs[n])
    return(cost[n]+min(minCost(cost,n-1), minCost(cost,n-2)))

cost=[20,15,30,5]
cost.append(0)
n=4
saved_costs=[-1,]*n
print("Minimum cost to reach the top is:",minCost(cost,n, saved_costs))
"""
# Time complexity: O(N)
# Space complexity: O(N)

# Step 3: Writing an iterative solution

cost=[20,15,30,5]
n=4
first_cost=cost[0]
second_cost=cost[1]
for i in range(2,n):
    calc_cost=cost[i]+min(first_cost,second_cost)
    first_cost=second_cost
    second_cost=calc_cost
print(min(first_cost,second_cost))

# Time complexity: O(N)
# Space complexity: O(1)