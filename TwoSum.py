nums = [15, 0, 7, 12,3, 7, 8, 9]
target = 9

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])