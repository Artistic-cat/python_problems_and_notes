#All pairs of integers who's sum is equal to a given number
num_list=[1,2,3,4,5,6]
target=11
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i]+num_list[j]==target:
            print([i,j])
            break
        else:
            continue
