"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500

Logic: Sum of remainders of both the numbers with 60 should be 0 or 60
"""

time = [30,20,150,100,40]

count=0
remainders=dict()
for i in range(len(time)):
    remainder=time[i]%60
    if (remainder==0 and (0 in remainders)):
        count+=remainders[remainder]
    if(60-remainder) in remainders:
        count+=remainders[60-remainder]
    if (remainder) in remainders:
        remainders[remainder]+=1
    else:
        remainders[remainder]=1
print(remainders)
print(count)

# Complexity: O(n)